"""Finite checks of the two CRT reconstructions and the auxiliary bits (Python 3.10+)."""

from itertools import product
from math import prod


def bits(length):
    return product((0, 1), repeat=length)


def entry(factor, assignment):
    ports, table = factor
    index = 0
    for port in ports:
        index = 2 * index + assignment[port]
    return table[index]


def edges(network):
    return sorted({edge for ports, _ in network for edge in ports})


def direct(network):
    labels = edges(network)
    return sum(prod(entry(f, dict(zip(labels, x))) for f in network) for x in bits(len(labels)))


def bases(height):
    limit = 4 * (height + 2)
    primes = []
    powers = []
    for candidate in range(2, limit + 1):
        if any(candidate % r == 0 for r in primes if r * r <= candidate):
            continue
        primes.append(candidate)
        power = candidate
        while power * candidate <= limit:
            power *= candidate
        powers.append(power)
    assert prod(powers) > 2 ** (height + 1)
    return powers


def crt(residues, moduli):
    value, period = 0, 1
    for residue, modulus in zip(residues, moduli, strict=True):
        digit = (residue - value) * pow(period, -1, modulus) % modulus
        value += period * digit
        period *= modulus
    return value


def outer_tables(network, q):
    return [(ports, [v % q for v in table]) for ports, table in network]


def counter_count(reduced, p, block_size):
    blocks = [reduced[i:i + block_size] for i in range(0, len(reduced), block_size)]
    boundary = [sorted(e for e in edges(block)
                       if sum(ports.count(e) for ports, _ in block) == 1)
                for block in blocks]
    crossing = sorted(set().union(*boundary))
    counters = []
    for block, ports in zip(blocks, boundary):
        internal = sorted(set(edges(block)) - set(ports))
        table = {}
        for z in bits(len(ports)):
            fixed = dict(zip(ports, z))
            weight = 0
            for x in bits(len(internal)):
                assignment = fixed | dict(zip(internal, x))
                weight += prod(entry(f, assignment) for f in block)
            residue = weight % p
            table[z] = sum(y < residue for y in range(1 << (p - 1).bit_length()))
        counters.append(table)
    count = 0
    for x in bits(len(crossing)):
        assignment = dict(zip(crossing, x))
        count += prod(table[tuple(assignment[e] for e in ports)]
                      for table, ports in zip(counters, boundary))
    return count


def recover(network, block_size):
    for e in edges(network):
        assert sum(ports.count(e) for ports, _ in network) == 2
    assert all(len(table) == 1 << len(ports) for ports, table in network)
    edge_count = len(edges(network))
    height = edge_count + sum(max(1, max(map(abs, table)).bit_length()) for _, table in network)
    outer = bases(height)
    residues = []
    queries = 0
    for q in outer:
        reduced = outer_tables(network, q)
        inner = bases(1 + edge_count + len(network) * (q - 1).bit_length())
        counts = [counter_count(reduced, p, block_size) for p in inner]
        middle = crt([count % p for count, p in zip(counts, inner)], inner)
        assert middle == direct(reduced)
        residues.append(middle % q)
        queries += len(inner)
    modulus = prod(outer)
    answer = crt(residues, outer)
    if 2 * answer > modulus:
        answer -= modulus
    assert answer == direct(network)
    return queries


def main():
    if not __debug__:
        raise SystemExit("Run with Python assertions enabled.")
    path = [((0,), [35, -19]), ((0, 1), [5, -7, 9, 13]), ((1,), [-4, 11])]
    reduced = outer_tables(path, 11)
    mods = [5, 7, 13, 17]
    counts = [counter_count(reduced, p, 2) for p in mods]
    assert counts == [4, 0, 77, 21]
    assert crt([c % p for c, p in zip(counts, mods)], mods) == direct(reduced) == 259
    assert direct(path) == -5428 and direct(path) % 11 == 6
    fixtures = [
        path, [], [((), [0])], [((), [-(1 << 45) + 3]), ((), [7])],
        [((0, 0), [-5, 99, 70, 8])],
        [((0, 1), [1, -4, 8, -2]), ((1, 0), [5, -1, 3, 7])],
        [((0,), [5, -5]), ((0,), [1, 1]), ((), [-3])],
        [((0,), [1, -3]), ((1,), [4, -1]), ((0,), [5, 9]), ((1,), [0, 2])],
    ]
    calls = sum(recover(net, size) for net in fixtures for size in (1, 2, 3))
    print(f"Passed {len(fixtures)} fixtures at three block sizes and {calls} unweighted counts.")
    print("Worked example: counts 4, 0, 77, 21; inner integer 259; signed answer -5428.")


if __name__ == "__main__":
    main()

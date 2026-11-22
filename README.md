# Removing integer weights from Boolean tensor networks with a linear number of wires per query

Daniel Fredriksen, Quantyra Inc. · [Manuscript PDF](manuscript.pdf) · [LaTeX source](manuscript.tex) · [ORCID](https://orcid.org/0009-0002-9123-7435)

An explicitly written network of bounded-arity signed integer tensors can be evaluated with polynomially many unweighted counting queries. The number of wires in each query grows linearly with the number of original tensors, even if one coefficient occupies most of the input. The target predicates have logarithmic arity. The proof groups tensors before encoding their weights as counts and reconstructs integers at two levels.

Assuming the [stated Boolean contraction theorem](https://github.com/openai/math/blob/7ef5c0cc5ca4b0e072b7a050fca09ab24bc6fa3a/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/build/quantitative-reduction.tex), the reduction gives a deterministic subexponential-time, polynomial-space algorithm. In the circuit application, the exponential term depends on two-qubit gate count. The paper gives the fixed gate set, exact output representation and comparisons with previous time and space bounds.

## Reproduce the checks

Run the following command from the repository root with Python 3.10 or later and assertions enabled.

~~~sh
python -B checks/exact_reduction.py
~~~

The checker reconstructs the signed contraction on eight small fixtures at three block sizes. It deliberately exercises the modular gadget even when direct enumeration would be cheaper. The reference sums the original integer tables. The private bits are counted block by block. These finite checks address the arithmetic, including signs, loops, parallel edges and zero counts. They use exhaustive enumeration as their counting backend.

To reproduce the PDF, set `SOURCE_DATE_EPOCH=1795219200` and run `tectonic manuscript.tex` with Tectonic 0.17.0. The [review record](review.md) gives the scope of the automated checks. The [Lean certification plan](lean-certification-plan.md) identifies the proposed first theorem and the external assumptions.

The preprint and supporting files are distributed under [CC BY 4.0](LICENSE).

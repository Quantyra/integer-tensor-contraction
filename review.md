# Review of version 1.0.0

Claude, AGY and Grok each reviewed the full manuscript, requested revisions and returned **RELEASE** on the same final LaTeX source. These were automated preprint reviews. The reviewers checked the implications from the stated premises. The release audit separately opened the primary sources used for comparison.

| Lens | Issue raised | Disposition |
| --- | --- | --- |
| Claude, proof and quantifiers | Distinguish the unconditional reduction from the external fast algorithm. Verify the prime-power bounds, branch for very long inputs, zero counts, signed uniqueness and incidence conventions. | The abstract states the distinction immediately. Section 2 specifies which crossing ports each block reads and gives the query and table sizes. Section 3 identifies Appendix D, Theorem D.1 and instantiates its hypotheses. |
| AGY, resources and reproducibility | Account for the intermediate precision, query count, gate ordering and storage at a cut. Recompute the signed example. | The text derives the inner height from the input-length branch, counts the oracle calls and specifies chronological cuts. It treats the controlled adjoint, gate-only projector expansion and exact readout. In the example the integer 259 lies below the bound 4000, which is smaller than the modulus product 7735. |
| Grok, adversarial scope and comparison | Test whether a per-factor counter gives the same wire count. Distinguish an oracle count from its congruence. Check the imported resource parameters, depth recurrence and overlap with prior work. | The paper gives the private-wire count for each construction, reduces each returned count before inner CRT, and writes out both the contraction theorem's parameters and the bit-length recurrence. The depth application is explicitly attributed to earlier methods as well. |

The pinned contraction theorem permits any fixed positive constants in its hypotheses. Taking its edge and precision constant to be one is therefore a valid instantiation. This resolves an optional question about that choice. The comparison covers Wang's Lemma 1 and Remark 2, Bhattacharjee's Theorem 5.3 and Lemma 5.5, and Tulsyan's Theorems 1.1 and 1.2. Historical priority remains unverified. [Pinned contraction theorem](https://github.com/openai/math/blob/7ef5c0cc5ca4b0e072b7a050fca09ab24bc6fa3a/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/build/quantitative-reduction.tex) · [Wang](https://optimization-online.org/wp-content/uploads/2026/11/main-1.pdf) · [Bhattacharjee](https://hexagonmath.org/pdf/2610.00594v1) · [Tulsyan](https://hexagonmath.org/pdf/2611.00090v1)

The standard-library checker passed eight fixtures with three different block sizes, for 7,320 unweighted counts. It reproduced the worked example's four distinct counts and its final signed integer. The six-page PDF rebuilt byte for byte in a separate directory; page bounds, references and citation metadata were checked. These results cover the finite arithmetic and release package. The general size bounds have a written proof. The external fast engine has no implementation or independent proof replay in this release.

| Item | SHA-256 |
| --- | --- |
| Reviewed LaTeX | `b51b62ccf555f8b9120921002da12f33291673fbc3908768af6da1d23eafdcbc` |
| Distributed PDF | `bd3e15f6bf81f4162c14a244ea7c9904c57f491653d03128142eabffb44e7b4c` |
| Claude's final report | `538514cd3c4b981ea83e7cfc779dd6d9aa3d45d508b25e0433086a4569ba9c03` |
| AGY's final report | `4ad861c02f91c3307b551b2c5e253362dfc2677624a47f50b7abff90fe71d8da` |
| Grok's final report | `0166e602f78f6465701e42254de7426a99636586971e88cd1a9474695a7eb89d` |

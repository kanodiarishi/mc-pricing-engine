# Learning log

One entry per working session. This is the raw material for explaining the project
later, so it records understanding rather than progress — what was taught, what landed,
and what did not.

The last section of each entry is the important one. An honest "I could reproduce the
algebra but I could not say why the measure change is legitimate" is worth more here
than a claim of full understanding, because it is the list of things to return to.

Mathematics belongs in `docs/theory/`, not here.

---

## Session 1 — 2026-09-21 — Stage 0: repository and environment

**Covered:** No mathematics. Project scaffolding only: `src/` layout, `pyproject.toml`,
`uv`-managed environment pinned to Python 3.12, `pytest`, `ruff`, `mypy`, GitHub Actions
CI, and the public repository — created before any pricing code exists, deliberately.

**Decisions made, and why:**

- *Hand-roll the inverse normal CDF and the Sobol generator; no `scipy`.* Chosen for
  learning value. Sobol construction is a concept this project is meant to teach, so
  importing it would hollow out Stage 4. Costs roughly five extra hours.
- *The inverse normal CDF belongs in Stage 1, not Stage 4.* Consequence of the above.
  If samplers emit uniforms and normals always come from `ppf(u)`, then pseudo-random
  and Sobol sampling become interchangeable, antithetic variates reduce to `u → 1−u`,
  and common random numbers for Greeks come free. Had Stage 1 drawn normals directly,
  the sampler interface would have had to be rebuilt in Stage 4.
- *Every pricer gets a scalar reference implementation, kept permanently as a test
  oracle for the vectorised version.* Resolves the tension between "correctness before
  speed" and needing enough paths to see convergence behaviour at all.
- *Only minimal seams in Stage 1 — Sampler, PathGenerator, Payoff.* The variance
  reduction layer waits for Stage 3, when there is a real requirement to design
  against rather than a guessed one.
- *No third-party test oracle.* The inverse CDF is checked by round-tripping against
  `math.erf`; Sobol will be checked against the equidistribution property that defines
  it. Both are stronger tests than comparison against another approximation, and they
  keep the Stage 7 QuantLib comparison genuinely independent.
- *`N803`/`N806` disabled in `ruff`.* Mathematical notation (`S0`, `K`, `T`) is easier
  to check against a derivation than PEP 8 naming would be.

**What landed:**

_(to complete)_

**What did not land / to revisit:**

_(to complete)_

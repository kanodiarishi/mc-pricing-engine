# Variance Reduction in Practice

**A Monte Carlo engine for path-dependent and structured equity payoffs.**

Prices European, Asian, barrier and autocallable equity derivatives under geometric
Brownian motion, then implements variance reduction properly: antithetic variates,
control variates, and quasi-Monte Carlo with Sobol sequences.

The headline deliverable is not the prices. It is the **convergence and efficiency
study**: how much accuracy each technique buys per unit of compute, per payoff type.
A technique that halves variance but triples runtime is worse than useless, and most
write-ups never measure this.

---

## Status

🚧 **Stage 0 — repository and environment.** No pricing code yet.

| Stage | Topic | Status |
|------:|-------|--------|
| 0 | Repository and environment | in progress |
| 1 | Risk-neutral pricing and European options | not started |
| 2 | Path dependence and discretisation | not started |
| 3 | Variance reduction | not started |
| 4 | Quasi-Monte Carlo | not started |
| 5 | Greeks | not started |
| 6 | Autocallable note | not started |
| 7 | Packaging and documentation | not started |

---

## Design commitments

These are deliberate, and each is defended in `docs/theory/`:

- **Nothing borrowed.** No QuantLib, no `py_vollib`, no `scipy`. The inverse normal CDF
  and the Sobol generator are implemented from first principles. Runtime dependencies
  are `numpy` and `matplotlib` only — the normal CDF comes from `math.erf` in the
  standard library. A single third-party cross-check against QuantLib appears in
  Stage 7, and is the first outside code to touch the project.
- **Samplers emit uniforms, never normals.** Normals always come from `ppf(u)`. This
  makes pseudo-random and Sobol sampling interchangeable, makes antithetic variates
  fall out as `u → 1−u`, and makes common random numbers for Greeks trivial.
- **Every pricer has a scalar reference implementation.** Written first, obviously
  correct by inspection, retained permanently as a test oracle for the vectorised
  version.
- **Deterministic.** Explicit seeding throughout; every reported number reproduces
  exactly.

## Install

```bash
uv sync
```

## Development

```bash
uv run pytest
uv run ruff check
uv run mypy src
```

## Licence

MIT — see [LICENSE](LICENSE).

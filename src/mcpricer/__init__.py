"""A Monte Carlo engine for path-dependent and structured equity derivatives.

The package is built up stage by stage. Each subpackage arrives with the concept it
implements, and the derivations behind it live in ``docs/theory/``:

- ``numerics``   -- numerical primitives (normal CDF and its inverse, Sobol sequences)
- ``sampling``   -- sources of uniform variates (pseudo-random, quasi-random)
- ``paths``      -- turning uniforms into asset price paths under GBM
- ``payoffs``    -- contract definitions evaluated on those paths
- ``analytic``   -- closed-form prices used as references for validation
- ``estimators`` -- variance reduction layered over any payoff
- ``greeks``     -- sensitivity estimation
- ``study``      -- the convergence and efficiency study

One architectural commitment runs through all of it: **samplers emit uniforms, never
normals.** Normals are always produced by applying the inverse normal CDF. That single
choice is what lets quasi-random sampling substitute for pseudo-random sampling without
touching a pricer, makes antithetic variates a transformation on the uniforms, and makes
common random numbers straightforward for finite-difference Greeks.
"""

__version__ = "0.1.0"

__all__ = ["__version__"]

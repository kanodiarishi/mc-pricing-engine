"""Checks that the package is assembled correctly.

There is no pricing code yet, so these tests guard the packaging itself: that the
installed package is importable, that it ships its type marker, and that the version
recorded in ``pyproject.toml`` has not drifted from the one exposed at runtime.

The version test is the only non-obvious one. Declaring a version in two places is a
standing invitation for them to disagree, and a stale ``__version__`` silently
mislabels every figure and result the package produces. Rather than remove one of the
two declarations, the mismatch is made a test failure.
"""

from __future__ import annotations

import tomllib
from pathlib import Path

import pytest

import mcpricer

PYPROJECT = Path(__file__).resolve().parent.parent / "pyproject.toml"


def test_package_imports() -> None:
    assert mcpricer.__version__


def test_type_marker_is_present() -> None:
    """``py.typed`` tells type checkers that our annotations are meant to be used."""
    marker = Path(mcpricer.__file__).parent / "py.typed"
    assert marker.exists(), "py.typed missing; downstream mypy would ignore our types"


@pytest.mark.skipif(not PYPROJECT.exists(), reason="not running from a source checkout")
def test_version_matches_pyproject() -> None:
    declared = tomllib.loads(PYPROJECT.read_text())["project"]["version"]
    assert mcpricer.__version__ == declared

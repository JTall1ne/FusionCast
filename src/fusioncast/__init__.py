"""FusionCast core package."""

from __future__ import annotations

from importlib import metadata

__all__ = ["__version__"]


def _load_version() -> str:
    try:
        return metadata.version("fusioncast")
    except metadata.PackageNotFoundError:  # pragma: no cover
        # Package is not installed; return a default placeholder version.
        return "0.0.0"


__version__ = _load_version()

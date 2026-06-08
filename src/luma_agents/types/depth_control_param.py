# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["DepthControlParam"]


class DepthControlParam(TypedDict, total=False):
    """Depth / scene-geometry conditioning control"""

    blur: Optional[float]
    """Depth-map blur amount from 0 to 1. Higher values allow more geometric freedom."""

    enabled: Optional[bool]
    """Enable or disable depth conditioning. Omit to use the model default."""

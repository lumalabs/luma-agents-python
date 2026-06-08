# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["TrajectoryControlParam"]


class TrajectoryControlParam(TypedDict, total=False):
    """Motion-trajectory conditioning control"""

    enabled: Optional[bool]
    """Enable or disable trajectory conditioning. Omit to use the model default."""

    sparsity: Optional[float]
    """Point-trajectory sparsity from 0 to 1. Higher values use fewer motion anchors."""

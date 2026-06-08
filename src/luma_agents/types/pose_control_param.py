# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .pose_control_strength import PoseControlStrength

__all__ = ["PoseControlParam"]


class PoseControlParam(TypedDict, total=False):
    """Pose / skeleton conditioning control"""

    enabled: Optional[bool]
    """Enable or disable pose conditioning. Omit to use the model default."""

    strength: Optional[PoseControlStrength]
    """Pose-conditioning strength"""

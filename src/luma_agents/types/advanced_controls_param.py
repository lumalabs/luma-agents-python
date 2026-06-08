# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .face_control_param import FaceControlParam
from .pose_control_param import PoseControlParam
from .depth_control_param import DepthControlParam
from .normals_control_param import NormalsControlParam
from .trajectory_control_param import TrajectoryControlParam

__all__ = ["AdvancedControlsParam"]


class AdvancedControlsParam(TypedDict, total=False):
    """Per-signal manual conditioning controls for video edits"""

    depth: Optional[DepthControlParam]
    """Depth / scene-geometry conditioning control"""

    face: Optional[FaceControlParam]
    """Face-identity conditioning control"""

    normals: Optional[NormalsControlParam]
    """Surface-normals conditioning control"""

    pose: Optional[PoseControlParam]
    """Pose / skeleton conditioning control"""

    trajectory: Optional[TrajectoryControlParam]
    """Motion-trajectory conditioning control"""

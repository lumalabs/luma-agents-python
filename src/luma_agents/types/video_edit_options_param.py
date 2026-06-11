# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import TypedDict

from .image_ref_param import ImageRefParam
from .video_edit_strength import VideoEditStrength
from .advanced_controls_param import AdvancedControlsParam

__all__ = ["VideoEditOptionsParam"]


class VideoEditOptionsParam(TypedDict, total=False):
    """Ray 3.2 video-to-video edit controls.

    Only valid under `video.edit` when `type` is `video_edit`. The source video must be 18 seconds or shorter; output duration matches the source.
    """

    auto_controls: Optional[bool]
    """When true, the model derives the control schedule from the source video.

    When omitted, supplying strength or controls implies manual mode.
    """

    controls: Optional[AdvancedControlsParam]
    """Per-signal manual conditioning controls for video edits"""

    keyframe_indexes: Optional[Iterable[int]]
    """
    Parallel list of non-negative, unique frame positions in the source video's
    frame grid where each keyframes[i] is anchored. Must match keyframes in length.
    """

    keyframes: Optional[Iterable[ImageRefParam]]
    """
    Multi-anchor guide-frame images at arbitrary source-frame positions (parallel
    with keyframe_indexes). Up to 64 anchors. Mutually exclusive with
    video.start_frame (the single-anchor case). Each entry takes the same ImageRef
    shape as source / image_ref[].
    """

    strength: Optional[VideoEditStrength]
    """How much a video edit preserves or reimagines the source"""

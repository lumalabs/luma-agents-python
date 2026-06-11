# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import TypedDict

from .video_duration import VideoDuration
from .image_ref_param import ImageRefParam
from .video_resolution import VideoResolution
from .source_position_param import SourcePositionParam
from .video_edit_options_param import VideoEditOptionsParam

__all__ = ["VideoOptionsParam"]


class VideoOptionsParam(TypedDict, total=False):
    """Ray 3.2 video request options.

    Common output settings live at the top level for `type=video`, `type=video_edit`, and `type=video_reframe`; video-to-video conditioning lives under `edit`.
    """

    duration: Optional[VideoDuration]
    """Video duration"""

    edit: Optional[VideoEditOptionsParam]
    """Ray 3.2 video-to-video edit controls.

    Only valid under `video.edit` when `type` is `video_edit`. The source video must
    be 18 seconds or shorter; output duration matches the source.
    """

    end_frame: Optional[ImageRefParam]
    """Media reference for guided generation.

    Provide exactly one of url, inline base64 data, or generation_id. URL/data
    references accept image media at image positions; video_edit and video_reframe
    sources also accept source.url or source.data when source.media_type is a
    video/\\** MIME. generation_id chains image_edit off a prior image output,
    video_edit/video_reframe off a prior video output, and
    video.start_frame/end_frame for extension.
    """

    exr_export: Optional[bool]
    """Export EXR alongside the MP4. Requires hdr=true."""

    hdr: Optional[bool]
    """Generate HDR video. Requires HDR access. Not supported for video_reframe."""

    keyframe_indexes: Optional[Iterable[int]]
    """
    Parallel list of non-negative, unique output-frame positions where each
    keyframes[i] is anchored, in the duration x 24fps grid (5s -> 0..120, 10s ->
    0..240). Must match keyframes in length.
    """

    keyframes: Optional[Iterable[ImageRefParam]]
    """
    Image-to-video guide frames (type=video only), each pinned to an output-frame
    position via the parallel keyframe_indexes. 1-64 anchors: a single anchor is a
    valid start-pinned i2v (an alternate to start_frame), and any count up to 64
    places guide frames at arbitrary positions. Unlike start_frame/end_frame (the
    legacy 2-frame surface), this supports arbitrary positions, 10s durations, and
    HDR. Mutually exclusive with start_frame / end_frame / loop. Only supported on
    model ray-3.2. For video-to-video keyframes use video.edit.keyframes on
    type=video_edit instead.
    """

    loop: Optional[bool]
    """Generate a seamlessly looping video.

    Only valid for type=video; not supported with duration=10s or hdr=true.
    """

    resolution: Optional[VideoResolution]
    """Ray 3.2 video output resolution.

    360p is the draft tier (fast, low-cost previews), accepted on type=video,
    video_edit, and video_reframe; on type=video it is SDR-only (not valid with
    hdr=true). 1080p is public for video generation; video_reframe 1080p is still
    rolling out and may return a coming-soon validation error until enabled for the
    caller.
    """

    source_position: Optional[SourcePositionParam]
    """Normalized source rectangle inside the output canvas for video_reframe.

    Omit to let the model choose the default centered-fit crop.
    """

    start_frame: Optional[ImageRefParam]
    """Media reference for guided generation.

    Provide exactly one of url, inline base64 data, or generation_id. URL/data
    references accept image media at image positions; video_edit and video_reframe
    sources also accept source.url or source.data when source.media_type is a
    video/\\** MIME. generation_id chains image_edit off a prior image output,
    video_edit/video_reframe off a prior video output, and
    video.start_frame/end_frame for extension.
    """

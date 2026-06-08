# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
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

    Only valid under `video.edit` when `type` is `video_edit`.
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

    loop: Optional[bool]
    """Generate a seamlessly looping video.

    Only valid for type=video; not supported with duration=10s or hdr=true.
    """

    resolution: Optional[VideoResolution]
    """Ray 3.2 video output resolution.

    1080p is public for video generation; video_reframe 1080p is still rolling out
    and may return a coming-soon validation error until enabled for the caller.
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

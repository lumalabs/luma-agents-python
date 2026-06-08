# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["ImageRefParam"]


class ImageRefParam(TypedDict, total=False):
    """Media reference for guided generation.

    Provide exactly one of url, inline base64 data, or generation_id. URL/data references accept image media at image positions; video_edit and video_reframe sources also accept source.url or source.data when source.media_type is a video/* MIME. generation_id chains image_edit off a prior image output, video_edit/video_reframe off a prior video output, and video.start_frame/end_frame for extension.
    """

    data: Optional[str]
    """Base64-encoded image or video data"""

    generation_id: Optional[str]
    """UUID of a prior generation owned by the same caller.

    Used on source for image_edit, video_edit, and video_reframe chaining and on
    video.start_frame / video.end_frame for video extension.
    """

    media_type: Optional[str]
    """MIME type (for example, image/jpeg or video/mp4).

    Required with data. Required with source.url on video_edit/video_reframe so the
    route can dispatch video ingest before fetching bytes; optional for image URLs.
    """

    url: Optional[str]
    """
    Publicly accessible image URL, or a video URL when used as source for
    video_edit/video_reframe with media_type=video/\\**.
    """

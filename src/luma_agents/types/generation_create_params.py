# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .model import Model
from .image_ref_param import ImageRefParam
from .video_options_param import VideoOptionsParam

__all__ = ["GenerationCreateParams"]


class GenerationCreateParams(TypedDict, total=False):
    prompt: Required[str]
    """Text prompt"""

    aspect_ratio: Optional[
        Literal["3:1", "2:1", "21:9", "16:9", "4:3", "3:2", "1:1", "3:4", "2:3", "9:16", "1:2", "1:3"]
    ]
    """Output aspect ratio.

    Valid values depend on the selected model and generation type; the server
    validates the final model-specific set.
    """

    image_ref: Iterable[ImageRefParam]
    """Reference images for style/content guidance.

    Up to 9 for type 'image', up to 8 for type 'image_edit'.
    """

    model: Model
    """Model identifier.

    `uni-1` is the default image tier; `uni-1-max` produces higher-quality output
    than `uni-1` at a higher per-image price. `ray-3.2` is the public video model
    for text-to-video, image-to-video, and video-to-video editing.
    """

    output_format: Optional[Literal["png", "jpeg"]]
    """Output image format"""

    source: Optional[ImageRefParam]
    """Media reference for guided generation.

    Provide exactly one of url, inline base64 data, or generation_id. URL/data
    references accept image media at image positions; video_edit and video_reframe
    sources also accept source.url or source.data when source.media_type is a
    video/\\** MIME. generation_id chains image_edit off a prior image output,
    video_edit/video_reframe off a prior video output, and
    video.start_frame/end_frame for extension.
    """

    style: Literal["auto", "manga"]
    """Style preset (auto, manga)"""

    type: Literal["image", "image_edit", "video", "video_edit", "video_reframe"]
    """The kind of generation to perform"""

    user_id: Optional[str]
    """Your end-user's stable opaque identifier (no PII).

    Forwarded to upstream model providers as their per-user tagging field so trust &
    safety violations can be attributed to a specific end-user rather than the whole
    API account. Also used for per-end-user usage breakdowns in /v1/usage. Strongly
    recommended for partner integrations.
    """

    video: Optional[VideoOptionsParam]
    """Ray 3.2 video request options.

    Common output settings live at the top level for `type=video`,
    `type=video_edit`, and `type=video_reframe`; video-to-video conditioning lives
    under `edit`.
    """

    web_search: bool
    """
    Enable web search grounding — the agent can search the web and download
    reference images before generating.
    """

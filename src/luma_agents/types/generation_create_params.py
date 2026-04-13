# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["GenerationCreateParams", "ImageRef", "Source"]


class GenerationCreateParams(TypedDict, total=False):
    prompt: Required[str]
    """Text prompt"""

    aspect_ratio: Optional[Literal["3:1", "2:1", "16:9", "3:2", "1:1", "2:3", "9:16", "1:2", "1:3"]]
    """Output aspect ratio"""

    image_ref: Iterable[ImageRef]
    """Reference images for style/content guidance. Up to 8 reference images."""

    model: str
    """Model to use"""

    output_format: Optional[Literal["png", "jpeg"]]
    """Output image format"""

    source: Optional[Source]
    """Reference image for guided generation.

    Provide either url or inline base64 data (not both).
    """

    style: Literal["auto", "manga"]
    """Style preset (auto, manga)"""

    type: Literal["image", "image_edit"]
    """The kind of generation to perform"""

    web_search: bool
    """
    Enable web search grounding — the agent can search the web and download
    reference images before generating.
    """


class ImageRef(TypedDict, total=False):
    """Reference image for guided generation.

    Provide either url or inline base64 data (not both).
    """

    data: Optional[str]
    """Base64-encoded image data"""

    media_type: Optional[str]
    """MIME type (e.g. image/jpeg). Required with data."""

    url: Optional[str]
    """Publicly accessible image URL"""


class Source(TypedDict, total=False):
    """Reference image for guided generation.

    Provide either url or inline base64 data (not both).
    """

    data: Optional[str]
    """Base64-encoded image data"""

    media_type: Optional[str]
    """MIME type (e.g. image/jpeg). Required with data."""

    url: Optional[str]
    """Publicly accessible image URL"""

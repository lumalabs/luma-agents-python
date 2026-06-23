# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .file_purpose import FilePurpose

__all__ = ["FileCreateParams"]


class FileCreateParams(TypedDict, total=False):
    mime_type: Required[str]
    """MIME type of the bytes you will upload."""

    size_bytes: Required[int]
    """Exact size in bytes of the object you will PUT.

    Up to 5 GiB (the S3 single-PUT ceiling).
    """

    expires_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Optional TTL.

    After this time Luma may automatically delete the file and reclaim its bytes.
    """

    filename: Optional[str]
    """Optional original filename to record."""

    purpose: FilePurpose
    """How the file is intended to be used in a generation.

    `input` is the primary subject (e.g. the source image for an edit); `reference`
    is style/content guidance.
    """

    user_id: Optional[str]
    """Optional opaque end-user tag for abuse attribution.

    Mirrors the user_id field on POST /generations.
    """

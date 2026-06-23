# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .file_state import FileState
from .file_purpose import FilePurpose

__all__ = ["File"]


class File(BaseModel):
    """A file in the caller's namespace."""

    id: str
    """File identifier, referenced as ImageRef.file_id."""

    created_at: datetime
    """Creation timestamp."""

    mime_type: str
    """MIME type of the stored bytes (for example, image/jpeg)."""

    purpose: FilePurpose
    """How the file is intended to be used in a generation.

    `input` is the primary subject (e.g. the source image for an edit); `reference`
    is style/content guidance.
    """

    size_bytes: int
    """Size of the stored object in bytes."""

    state: FileState
    """Lifecycle state of an uploaded file.

    `pending` until bytes are received and the ingest pipeline runs; `ready` once it
    can be referenced from a generation; `failed` if ingest/moderation rejected it;
    `deleted` after a soft-delete.
    """

    deleted_at: Optional[datetime] = None
    """Soft-delete timestamp, if the file was deleted."""

    expires_at: Optional[datetime] = None
    """TTL set at upload, if any.

    After this time Luma may automatically delete the file and reclaim its bytes —
    you don't need to call DELETE yourself.
    """

    failure_reason: Optional[str] = None
    """Human-readable reason when state is failed."""

    filename: Optional[str] = None
    """Original filename supplied at upload, if any."""

    user_id: Optional[str] = None
    """The opaque end-user tag supplied at upload, echoed back unchanged.

    Abuse-attribution only; not an access-control primitive.
    """

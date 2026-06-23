# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .file import File
from .._models import BaseModel
from .file_state import FileState
from .presigned_upload import PresignedUpload

__all__ = ["CreateFileResponse"]


class CreateFileResponse(BaseModel):
    """Result of POST /files.

    In the multipart (inline) flow `upload` is null and the file is already `pending` ingest. In the presigned (JSON) flow `upload` carries the PUT envelope and the file stays `pending` until you call POST /files/{file_id}/complete. Top-level `id` and `state` are conveniences that mirror `file.id` and `file.state`; the full record is always under `file`.
    """

    id: str
    """File identifier."""

    file: File
    """A file in the caller's namespace."""

    state: FileState
    """Lifecycle state of an uploaded file.

    `pending` until bytes are received and the ingest pipeline runs; `ready` once it
    can be referenced from a generation; `failed` if ingest/moderation rejected it;
    `deleted` after a soft-delete.
    """

    upload: Optional[PresignedUpload] = None
    """Where to PUT the file bytes for a presigned (JSON) upload.

    Issue an HTTP PUT of the raw bytes to `url` with the given `headers`, then call
    POST /files/{file_id}/complete.
    """

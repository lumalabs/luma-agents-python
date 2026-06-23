# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["PresignedUpload"]


class PresignedUpload(BaseModel):
    """Where to PUT the file bytes for a presigned (JSON) upload.

    Issue an HTTP PUT of the raw bytes to `url` with the given `headers`, then call POST /files/{file_id}/complete.
    """

    expires_at: datetime
    """When the presigned URL expires."""

    method: str
    """HTTP method to use for the upload — always PUT."""

    url: str
    """Presigned S3 URL to PUT the bytes to."""

    headers: Optional[Dict[str, str]] = None
    """Headers that must be sent with the PUT request."""

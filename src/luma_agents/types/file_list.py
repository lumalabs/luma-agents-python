# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .file import File
from .._models import BaseModel

__all__ = ["FileList"]


class FileList(BaseModel):
    """Keyset-paginated page of files, newest first.

    When has_more is true, pass next_cursor back as the cursor query parameter to fetch the next page. next_cursor is opaque.
    """

    data: List[File]
    """Files in this page."""

    has_more: bool
    """Whether more files exist beyond this page."""

    next_cursor: Optional[str] = None
    """Opaque cursor for the next page, when has_more is true."""

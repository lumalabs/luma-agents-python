# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .file_state import FileState
from .file_purpose import FilePurpose

__all__ = ["FileListParams"]


class FileListParams(TypedDict, total=False):
    cursor: str
    """Opaque pagination cursor from a prior response's next_cursor."""

    limit: int
    """Maximum files to return (1–100). Defaults to 25."""

    purpose: FilePurpose
    """Filter to files with this purpose."""

    state: FileState
    """Filter to files in this state."""

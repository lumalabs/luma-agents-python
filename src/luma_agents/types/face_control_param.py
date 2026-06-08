# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["FaceControlParam"]


class FaceControlParam(TypedDict, total=False):
    """Face-identity conditioning control"""

    enabled: Optional[bool]
    """Enable or disable face conditioning. Omit to use the model default."""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["NormalsControlParam"]


class NormalsControlParam(TypedDict, total=False):
    """Surface-normals conditioning control"""

    augmentation: Optional[float]
    """Surface-normals augmentation from 0 to 1.

    Higher values allow more reinterpretation of surface geometry.
    """

    enabled: Optional[bool]
    """Enable or disable normals conditioning. Omit to use the model default."""

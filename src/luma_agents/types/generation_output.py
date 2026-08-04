# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["GenerationOutput", "Layer"]


class Layer(BaseModel):
    """Per-layer semantics for a type=layering output"""

    alpha_hint: str
    """
    Edge treatment of the layer's transparency — soft (hair/fur/glass), hard (solid
    edges), or none (the opaque background)
    """

    description: str
    """Complete-element caption for the layer's content"""

    index: int
    """Layer position, front-to-back; the last layer is the background"""

    label: str
    """Short (1-2 word) layer name"""


class GenerationOutput(BaseModel):
    """A single generated output"""

    type: str
    """Media type (e.g. image, video)"""

    url: str
    """Presigned URL (1hr expiry)"""

    layer: Optional[Layer] = None
    """Per-layer semantics for a type=layering output"""

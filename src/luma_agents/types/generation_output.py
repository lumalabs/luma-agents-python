# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["GenerationOutput", "Layer", "LayerBounds"]


class LayerBounds(BaseModel):
    """Where a layer's returned pixels sit inside the full composite frame.

    Layer images are cropped to their visible-alpha bounding box, so layers of one stack have differing pixel dimensions. Composite onto a transparent canvas_width x canvas_height image by pasting each layer at (x, y), iterating the output list in reverse (back-to-front), to reconstruct the source frame.
    """

    canvas_height: int
    """Height of the full composite canvas the layers reassemble into"""

    canvas_width: int
    """Width of the full composite canvas the layers reassemble into"""

    height: int
    """Pixel height of the returned layer image"""

    width: int
    """Pixel width of the returned layer image"""

    x: int
    """Left offset of this layer's pixels within the composite canvas"""

    y: int
    """Top offset of this layer's pixels within the composite canvas"""


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

    bounds: Optional[LayerBounds] = None
    """Where a layer's returned pixels sit inside the full composite frame.

    Layer images are cropped to their visible-alpha bounding box, so layers of one
    stack have differing pixel dimensions. Composite onto a transparent canvas_width
    x canvas_height image by pasting each layer at (x, y), iterating the output list
    in reverse (back-to-front), to reconstruct the source frame.
    """


class GenerationOutput(BaseModel):
    """A single generated output"""

    type: str
    """Media type (e.g. image, video)"""

    url: str
    """Presigned URL (1hr expiry)"""

    layer: Optional[Layer] = None
    """Per-layer semantics for a type=layering output"""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Generation", "Output"]


class Output(BaseModel):
    """A single generated output"""

    type: str
    """Media type (e.g. image)"""

    url: str
    """Presigned URL (1hr expiry)"""


class Generation(BaseModel):
    """Generation status and output"""

    id: str
    """Generation identifier"""

    created_at: str
    """Creation timestamp"""

    model: str
    """Model used"""

    state: Literal["queued", "processing", "completed", "failed"]
    """Current state of the generation"""

    type: Literal["image", "image_edit"]
    """The kind of generation to perform"""

    failure_reason: Optional[str] = None
    """Error description (populated on failure)"""

    output: Optional[List[Output]] = None
    """Generated outputs (populated on completion)"""

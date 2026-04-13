# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .generation_output import GenerationOutput

__all__ = ["Generation"]


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

    failure_code: Optional[Literal["content_moderated", "generation_failed", "output_not_found"]] = None
    """Machine-readable failure code for programmatic handling"""

    failure_reason: Optional[str] = None
    """Human-readable failure description"""

    output: Optional[List[GenerationOutput]] = None
    """Generated outputs (populated on completion)"""

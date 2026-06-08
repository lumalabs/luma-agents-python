# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["GenerationOutput"]


class GenerationOutput(BaseModel):
    """A single generated output"""

    type: str
    """Media type (e.g. image, video)"""

    url: str
    """Presigned URL (1hr expiry)"""

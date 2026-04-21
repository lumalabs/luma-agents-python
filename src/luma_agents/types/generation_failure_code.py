# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["GenerationFailureCode"]

GenerationFailureCode: TypeAlias = Literal[
    "content_moderated", "generation_failed", "budget_exhausted", "output_not_found"
]

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SourcePositionParam"]


class SourcePositionParam(TypedDict, total=False):
    """Normalized source rectangle inside the output canvas for video_reframe.

    Omit to let the model choose the default centered-fit crop.
    """

    h_norm: Required[float]
    """Source rectangle height, as a fraction of canvas height.

    Up to 2.0 so the source can bleed off-canvas.
    """

    w_norm: Required[float]
    """Source rectangle width, as a fraction of canvas width.

    Up to 2.0 so the source can bleed off-canvas.
    """

    x_norm: Required[float]
    """Left edge of the source rectangle, as a fraction of canvas width.

    May be negative when the source extends off-canvas.
    """

    y_norm: Required[float]
    """Top edge of the source rectangle, as a fraction of canvas height.

    May be negative when the source extends off-canvas.
    """

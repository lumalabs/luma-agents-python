# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal

import httpx

from ..types import Model, generation_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..types.model import Model
from .._base_client import make_request_options
from ..types.generation import Generation

__all__ = ["GenerationsResource", "AsyncGenerationsResource"]


class GenerationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GenerationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/luma-agents-python#accessing-raw-response-data-eg-headers
        """
        return GenerationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GenerationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/luma-agents-python#with_streaming_response
        """
        return GenerationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        prompt: str,
        aspect_ratio: Optional[Literal["3:1", "2:1", "16:9", "3:2", "1:1", "2:3", "9:16", "1:2", "1:3"]] | Omit = omit,
        image_ref: Iterable[generation_create_params.ImageRef] | Omit = omit,
        model: Model | Omit = omit,
        output_format: Optional[Literal["png", "jpeg"]] | Omit = omit,
        source: Optional[generation_create_params.Source] | Omit = omit,
        style: Literal["auto", "manga"] | Omit = omit,
        type: Literal["image", "image_edit"] | Omit = omit,
        user_id: Optional[str] | Omit = omit,
        web_search: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Generation:
        """Submit an image generation or edit job.

        Returns immediately with an opaque job
        ID to poll via GET /generations/{id}.

        Args:
          prompt: Text prompt

          aspect_ratio: Output aspect ratio

          image_ref: Reference images for style/content guidance. Up to 9 for type 'image', up to 8
              for type 'image_edit'.

          model: Model identifier. `uni-1` is the default tier; `uni-1-max` produces
              higher-quality output than `uni-1` at a higher per-image price. Both models are
              available to all accounts — see Pricing for per-image rates.

          output_format: Output image format

          source: Reference image for guided generation. Provide either url or inline base64 data
              (not both).

          style: Style preset (auto, manga)

          type: The kind of generation to perform

          user_id: Your end-user's stable opaque identifier (no PII). Forwarded to upstream model
              providers as their per-user tagging field so trust & safety violations can be
              attributed to a specific end-user rather than the whole API account. Also used
              for per-end-user usage breakdowns in /v1/usage. Strongly recommended for partner
              integrations.

          web_search: Enable web search grounding — the agent can search the web and download
              reference images before generating.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/generations",
            body=maybe_transform(
                {
                    "prompt": prompt,
                    "aspect_ratio": aspect_ratio,
                    "image_ref": image_ref,
                    "model": model,
                    "output_format": output_format,
                    "source": source,
                    "style": style,
                    "type": type,
                    "user_id": user_id,
                    "web_search": web_search,
                },
                generation_create_params.GenerationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Generation,
        )

    def get(
        self,
        generation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Generation:
        """Poll for generation status and output.

        On completion, the response includes
        presigned URLs to download the generated images.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not generation_id:
            raise ValueError(f"Expected a non-empty value for `generation_id` but received {generation_id!r}")
        return self._get(
            path_template("/generations/{generation_id}", generation_id=generation_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Generation,
        )


class AsyncGenerationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGenerationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/luma-agents-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGenerationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGenerationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/luma-agents-python#with_streaming_response
        """
        return AsyncGenerationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        prompt: str,
        aspect_ratio: Optional[Literal["3:1", "2:1", "16:9", "3:2", "1:1", "2:3", "9:16", "1:2", "1:3"]] | Omit = omit,
        image_ref: Iterable[generation_create_params.ImageRef] | Omit = omit,
        model: Model | Omit = omit,
        output_format: Optional[Literal["png", "jpeg"]] | Omit = omit,
        source: Optional[generation_create_params.Source] | Omit = omit,
        style: Literal["auto", "manga"] | Omit = omit,
        type: Literal["image", "image_edit"] | Omit = omit,
        user_id: Optional[str] | Omit = omit,
        web_search: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Generation:
        """Submit an image generation or edit job.

        Returns immediately with an opaque job
        ID to poll via GET /generations/{id}.

        Args:
          prompt: Text prompt

          aspect_ratio: Output aspect ratio

          image_ref: Reference images for style/content guidance. Up to 9 for type 'image', up to 8
              for type 'image_edit'.

          model: Model identifier. `uni-1` is the default tier; `uni-1-max` produces
              higher-quality output than `uni-1` at a higher per-image price. Both models are
              available to all accounts — see Pricing for per-image rates.

          output_format: Output image format

          source: Reference image for guided generation. Provide either url or inline base64 data
              (not both).

          style: Style preset (auto, manga)

          type: The kind of generation to perform

          user_id: Your end-user's stable opaque identifier (no PII). Forwarded to upstream model
              providers as their per-user tagging field so trust & safety violations can be
              attributed to a specific end-user rather than the whole API account. Also used
              for per-end-user usage breakdowns in /v1/usage. Strongly recommended for partner
              integrations.

          web_search: Enable web search grounding — the agent can search the web and download
              reference images before generating.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/generations",
            body=await async_maybe_transform(
                {
                    "prompt": prompt,
                    "aspect_ratio": aspect_ratio,
                    "image_ref": image_ref,
                    "model": model,
                    "output_format": output_format,
                    "source": source,
                    "style": style,
                    "type": type,
                    "user_id": user_id,
                    "web_search": web_search,
                },
                generation_create_params.GenerationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Generation,
        )

    async def get(
        self,
        generation_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Generation:
        """Poll for generation status and output.

        On completion, the response includes
        presigned URLs to download the generated images.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not generation_id:
            raise ValueError(f"Expected a non-empty value for `generation_id` but received {generation_id!r}")
        return await self._get(
            path_template("/generations/{generation_id}", generation_id=generation_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Generation,
        )


class GenerationsResourceWithRawResponse:
    def __init__(self, generations: GenerationsResource) -> None:
        self._generations = generations

        self.create = to_raw_response_wrapper(
            generations.create,
        )
        self.get = to_raw_response_wrapper(
            generations.get,
        )


class AsyncGenerationsResourceWithRawResponse:
    def __init__(self, generations: AsyncGenerationsResource) -> None:
        self._generations = generations

        self.create = async_to_raw_response_wrapper(
            generations.create,
        )
        self.get = async_to_raw_response_wrapper(
            generations.get,
        )


class GenerationsResourceWithStreamingResponse:
    def __init__(self, generations: GenerationsResource) -> None:
        self._generations = generations

        self.create = to_streamed_response_wrapper(
            generations.create,
        )
        self.get = to_streamed_response_wrapper(
            generations.get,
        )


class AsyncGenerationsResourceWithStreamingResponse:
    def __init__(self, generations: AsyncGenerationsResource) -> None:
        self._generations = generations

        self.create = async_to_streamed_response_wrapper(
            generations.create,
        )
        self.get = async_to_streamed_response_wrapper(
            generations.get,
        )

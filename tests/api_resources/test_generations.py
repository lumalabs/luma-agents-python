# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from luma_agents import Luma, AsyncLuma
from tests.utils import assert_matches_type
from luma_agents.types import Generation

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGenerations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Luma) -> None:
        generation = client.generations.create(
            prompt="A glass of iced coffee on a marble countertop, morning light streaming through a window",
        )
        assert_matches_type(Generation, generation, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Luma) -> None:
        generation = client.generations.create(
            prompt="A glass of iced coffee on a marble countertop, morning light streaming through a window",
            aspect_ratio="3:1",
            image_ref=[
                {
                    "data": "data",
                    "media_type": "media_type",
                    "url": "url",
                }
            ],
            model="model",
            output_format="png",
            source={
                "data": "data",
                "media_type": "media_type",
                "url": "url",
            },
            style="auto",
            type="image",
            user_id="user_id",
            web_search=True,
        )
        assert_matches_type(Generation, generation, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Luma) -> None:
        response = client.generations.with_raw_response.create(
            prompt="A glass of iced coffee on a marble countertop, morning light streaming through a window",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generation = response.parse()
        assert_matches_type(Generation, generation, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Luma) -> None:
        with client.generations.with_streaming_response.create(
            prompt="A glass of iced coffee on a marble countertop, morning light streaming through a window",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generation = response.parse()
            assert_matches_type(Generation, generation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Luma) -> None:
        generation = client.generations.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Generation, generation, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Luma) -> None:
        response = client.generations.with_raw_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generation = response.parse()
        assert_matches_type(Generation, generation, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Luma) -> None:
        with client.generations.with_streaming_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generation = response.parse()
            assert_matches_type(Generation, generation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Luma) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `generation_id` but received ''"):
            client.generations.with_raw_response.get(
                "",
            )


class TestAsyncGenerations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncLuma) -> None:
        generation = await async_client.generations.create(
            prompt="A glass of iced coffee on a marble countertop, morning light streaming through a window",
        )
        assert_matches_type(Generation, generation, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLuma) -> None:
        generation = await async_client.generations.create(
            prompt="A glass of iced coffee on a marble countertop, morning light streaming through a window",
            aspect_ratio="3:1",
            image_ref=[
                {
                    "data": "data",
                    "media_type": "media_type",
                    "url": "url",
                }
            ],
            model="model",
            output_format="png",
            source={
                "data": "data",
                "media_type": "media_type",
                "url": "url",
            },
            style="auto",
            type="image",
            user_id="user_id",
            web_search=True,
        )
        assert_matches_type(Generation, generation, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLuma) -> None:
        response = await async_client.generations.with_raw_response.create(
            prompt="A glass of iced coffee on a marble countertop, morning light streaming through a window",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generation = await response.parse()
        assert_matches_type(Generation, generation, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLuma) -> None:
        async with async_client.generations.with_streaming_response.create(
            prompt="A glass of iced coffee on a marble countertop, morning light streaming through a window",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generation = await response.parse()
            assert_matches_type(Generation, generation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncLuma) -> None:
        generation = await async_client.generations.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Generation, generation, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncLuma) -> None:
        response = await async_client.generations.with_raw_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generation = await response.parse()
        assert_matches_type(Generation, generation, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncLuma) -> None:
        async with async_client.generations.with_streaming_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generation = await response.parse()
            assert_matches_type(Generation, generation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncLuma) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `generation_id` but received ''"):
            await async_client.generations.with_raw_response.get(
                "",
            )

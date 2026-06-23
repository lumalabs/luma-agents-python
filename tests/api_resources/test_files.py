# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from luma_agents import Luma, AsyncLuma
from tests.utils import assert_matches_type
from luma_agents.types import (
    File,
    FileList,
    CreateFileResponse,
)
from luma_agents._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Luma) -> None:
        file = client.files.create(
            mime_type="x",
            size_bytes=1,
        )
        assert_matches_type(CreateFileResponse, file, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Luma) -> None:
        file = client.files.create(
            mime_type="x",
            size_bytes=1,
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            filename="filename",
            purpose="input",
            user_id="user_id",
        )
        assert_matches_type(CreateFileResponse, file, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Luma) -> None:
        response = client.files.with_raw_response.create(
            mime_type="x",
            size_bytes=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(CreateFileResponse, file, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Luma) -> None:
        with client.files.with_streaming_response.create(
            mime_type="x",
            size_bytes=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(CreateFileResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Luma) -> None:
        file = client.files.list()
        assert_matches_type(FileList, file, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Luma) -> None:
        file = client.files.list(
            cursor="cursor",
            limit=1,
            purpose="input",
            state="pending",
        )
        assert_matches_type(FileList, file, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Luma) -> None:
        response = client.files.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileList, file, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Luma) -> None:
        with client.files.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileList, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Luma) -> None:
        file = client.files.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert file is None

    @parametrize
    def test_raw_response_delete(self, client: Luma) -> None:
        response = client.files.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert file is None

    @parametrize
    def test_streaming_response_delete(self, client: Luma) -> None:
        with client.files.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert file is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Luma) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.files.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_complete(self, client: Luma) -> None:
        file = client.files.complete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(File, file, path=["response"])

    @parametrize
    def test_raw_response_complete(self, client: Luma) -> None:
        response = client.files.with_raw_response.complete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(File, file, path=["response"])

    @parametrize
    def test_streaming_response_complete(self, client: Luma) -> None:
        with client.files.with_streaming_response.complete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(File, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_complete(self, client: Luma) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.files.with_raw_response.complete(
                "",
            )

    @parametrize
    def test_method_get(self, client: Luma) -> None:
        file = client.files.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(File, file, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Luma) -> None:
        response = client.files.with_raw_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(File, file, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Luma) -> None:
        with client.files.with_streaming_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(File, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Luma) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.files.with_raw_response.get(
                "",
            )


class TestAsyncFiles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncLuma) -> None:
        file = await async_client.files.create(
            mime_type="x",
            size_bytes=1,
        )
        assert_matches_type(CreateFileResponse, file, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLuma) -> None:
        file = await async_client.files.create(
            mime_type="x",
            size_bytes=1,
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            filename="filename",
            purpose="input",
            user_id="user_id",
        )
        assert_matches_type(CreateFileResponse, file, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLuma) -> None:
        response = await async_client.files.with_raw_response.create(
            mime_type="x",
            size_bytes=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(CreateFileResponse, file, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLuma) -> None:
        async with async_client.files.with_streaming_response.create(
            mime_type="x",
            size_bytes=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(CreateFileResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncLuma) -> None:
        file = await async_client.files.list()
        assert_matches_type(FileList, file, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLuma) -> None:
        file = await async_client.files.list(
            cursor="cursor",
            limit=1,
            purpose="input",
            state="pending",
        )
        assert_matches_type(FileList, file, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLuma) -> None:
        response = await async_client.files.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileList, file, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLuma) -> None:
        async with async_client.files.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileList, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncLuma) -> None:
        file = await async_client.files.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert file is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLuma) -> None:
        response = await async_client.files.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert file is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLuma) -> None:
        async with async_client.files.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert file is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLuma) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.files.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_complete(self, async_client: AsyncLuma) -> None:
        file = await async_client.files.complete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(File, file, path=["response"])

    @parametrize
    async def test_raw_response_complete(self, async_client: AsyncLuma) -> None:
        response = await async_client.files.with_raw_response.complete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(File, file, path=["response"])

    @parametrize
    async def test_streaming_response_complete(self, async_client: AsyncLuma) -> None:
        async with async_client.files.with_streaming_response.complete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(File, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_complete(self, async_client: AsyncLuma) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.files.with_raw_response.complete(
                "",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncLuma) -> None:
        file = await async_client.files.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(File, file, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncLuma) -> None:
        response = await async_client.files.with_raw_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(File, file, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncLuma) -> None:
        async with async_client.files.with_streaming_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(File, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncLuma) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.files.with_raw_response.get(
                "",
            )

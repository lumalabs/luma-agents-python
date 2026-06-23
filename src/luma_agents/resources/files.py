# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Mapping, Optional, cast
from datetime import datetime

import httpx

from ..types import FileState, FilePurpose, file_list_params, file_create_params
from .._files import deepcopy_with_paths
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import extract_files, path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..types.file import File
from .._base_client import make_request_options
from ..types.file_list import FileList
from ..types.file_state import FileState
from ..types.file_purpose import FilePurpose
from ..types.create_file_response import CreateFileResponse

__all__ = ["FilesResource", "AsyncFilesResource"]


class FilesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lumalabs/luma-agents-python#accessing-raw-response-data-eg-headers
        """
        return FilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lumalabs/luma-agents-python#with_streaming_response
        """
        return FilesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        mime_type: str,
        size_bytes: int,
        expires_at: Union[str, datetime, None] | Omit = omit,
        filename: Optional[str] | Omit = omit,
        purpose: FilePurpose | Omit = omit,
        user_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreateFileResponse:
        """
        Upload a file to your namespace, then reference it from a generation via
        ImageRef.file_id (as source, image_ref[], video.start_frame, keyframes, and so
        on). Two upload modes share this endpoint, selected by Content-Type:

        - multipart/form-data — send the bytes inline in the `file` part. Best for small
          files (subject to an inline size cap; larger files must use the presigned
          flow). The returned file is already `pending` ingest.

        - application/json — request a presigned upload. The response `upload` envelope
          tells you where to PUT the bytes; afterward call POST
          /files/{file_id}/complete to start ingest. Use this for larger files.

        Args:
          mime_type: MIME type of the bytes you will upload.

          size_bytes: Exact size in bytes of the object you will PUT. Up to 5 GiB (the S3 single-PUT
              ceiling).

          expires_at: Optional TTL. After this time Luma may automatically delete the file and reclaim
              its bytes.

          filename: Optional original filename to record.

          purpose: How the file is intended to be used in a generation. `input` is the primary
              subject (e.g. the source image for an edit); `reference` is style/content
              guidance.

          user_id: Optional opaque end-user tag for abuse attribution. Mirrors the user_id field on
              POST /generations.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_with_paths(
            {
                "mime_type": mime_type,
                "size_bytes": size_bytes,
                "expires_at": expires_at,
                "filename": filename,
                "purpose": purpose,
                "user_id": user_id,
            },
            [["file"]],
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/files",
            body=maybe_transform(body, file_create_params.FileCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateFileResponse,
        )

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        purpose: FilePurpose | Omit = omit,
        state: FileState | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileList:
        """List the files in your namespace, newest first.

        Keyset-paginated: when has_more
        is true, pass next_cursor back as cursor.

        Args:
          cursor: Opaque pagination cursor from a prior response's next_cursor.

          limit: Maximum files to return (1–100). Defaults to 25.

          purpose: Filter to files with this purpose.

          state: Filter to files in this state.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/files",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "purpose": purpose,
                        "state": state,
                    },
                    file_list_params.FileListParams,
                ),
            ),
            cast_to=FileList,
        )

    def delete(
        self,
        file_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Soft-delete a file.

        It can no longer be referenced from new generations. Returns
        204 with no body.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/files/{file_id}", file_id=file_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def complete(
        self,
        file_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> File:
        """
        Finalize a presigned upload after you have PUT the bytes to the upload URL.
        Kicks off ingest/moderation and returns the file, which transitions to `ready`
        (or `failed`) asynchronously — poll GET /files/{file_id} to observe the terminal
        state.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return self._post(
            path_template("/files/{file_id}/complete", file_id=file_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=File,
        )

    def get(
        self,
        file_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> File:
        """
        Retrieve metadata for a single file in your namespace.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return self._get(
            path_template("/files/{file_id}", file_id=file_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=File,
        )


class AsyncFilesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lumalabs/luma-agents-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lumalabs/luma-agents-python#with_streaming_response
        """
        return AsyncFilesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        mime_type: str,
        size_bytes: int,
        expires_at: Union[str, datetime, None] | Omit = omit,
        filename: Optional[str] | Omit = omit,
        purpose: FilePurpose | Omit = omit,
        user_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreateFileResponse:
        """
        Upload a file to your namespace, then reference it from a generation via
        ImageRef.file_id (as source, image_ref[], video.start_frame, keyframes, and so
        on). Two upload modes share this endpoint, selected by Content-Type:

        - multipart/form-data — send the bytes inline in the `file` part. Best for small
          files (subject to an inline size cap; larger files must use the presigned
          flow). The returned file is already `pending` ingest.

        - application/json — request a presigned upload. The response `upload` envelope
          tells you where to PUT the bytes; afterward call POST
          /files/{file_id}/complete to start ingest. Use this for larger files.

        Args:
          mime_type: MIME type of the bytes you will upload.

          size_bytes: Exact size in bytes of the object you will PUT. Up to 5 GiB (the S3 single-PUT
              ceiling).

          expires_at: Optional TTL. After this time Luma may automatically delete the file and reclaim
              its bytes.

          filename: Optional original filename to record.

          purpose: How the file is intended to be used in a generation. `input` is the primary
              subject (e.g. the source image for an edit); `reference` is style/content
              guidance.

          user_id: Optional opaque end-user tag for abuse attribution. Mirrors the user_id field on
              POST /generations.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_with_paths(
            {
                "mime_type": mime_type,
                "size_bytes": size_bytes,
                "expires_at": expires_at,
                "filename": filename,
                "purpose": purpose,
                "user_id": user_id,
            },
            [["file"]],
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/files",
            body=await async_maybe_transform(body, file_create_params.FileCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateFileResponse,
        )

    async def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        purpose: FilePurpose | Omit = omit,
        state: FileState | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileList:
        """List the files in your namespace, newest first.

        Keyset-paginated: when has_more
        is true, pass next_cursor back as cursor.

        Args:
          cursor: Opaque pagination cursor from a prior response's next_cursor.

          limit: Maximum files to return (1–100). Defaults to 25.

          purpose: Filter to files with this purpose.

          state: Filter to files in this state.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/files",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "purpose": purpose,
                        "state": state,
                    },
                    file_list_params.FileListParams,
                ),
            ),
            cast_to=FileList,
        )

    async def delete(
        self,
        file_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Soft-delete a file.

        It can no longer be referenced from new generations. Returns
        204 with no body.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/files/{file_id}", file_id=file_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def complete(
        self,
        file_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> File:
        """
        Finalize a presigned upload after you have PUT the bytes to the upload URL.
        Kicks off ingest/moderation and returns the file, which transitions to `ready`
        (or `failed`) asynchronously — poll GET /files/{file_id} to observe the terminal
        state.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return await self._post(
            path_template("/files/{file_id}/complete", file_id=file_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=File,
        )

    async def get(
        self,
        file_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> File:
        """
        Retrieve metadata for a single file in your namespace.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return await self._get(
            path_template("/files/{file_id}", file_id=file_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=File,
        )


class FilesResourceWithRawResponse:
    def __init__(self, files: FilesResource) -> None:
        self._files = files

        self.create = to_raw_response_wrapper(
            files.create,
        )
        self.list = to_raw_response_wrapper(
            files.list,
        )
        self.delete = to_raw_response_wrapper(
            files.delete,
        )
        self.complete = to_raw_response_wrapper(
            files.complete,
        )
        self.get = to_raw_response_wrapper(
            files.get,
        )


class AsyncFilesResourceWithRawResponse:
    def __init__(self, files: AsyncFilesResource) -> None:
        self._files = files

        self.create = async_to_raw_response_wrapper(
            files.create,
        )
        self.list = async_to_raw_response_wrapper(
            files.list,
        )
        self.delete = async_to_raw_response_wrapper(
            files.delete,
        )
        self.complete = async_to_raw_response_wrapper(
            files.complete,
        )
        self.get = async_to_raw_response_wrapper(
            files.get,
        )


class FilesResourceWithStreamingResponse:
    def __init__(self, files: FilesResource) -> None:
        self._files = files

        self.create = to_streamed_response_wrapper(
            files.create,
        )
        self.list = to_streamed_response_wrapper(
            files.list,
        )
        self.delete = to_streamed_response_wrapper(
            files.delete,
        )
        self.complete = to_streamed_response_wrapper(
            files.complete,
        )
        self.get = to_streamed_response_wrapper(
            files.get,
        )


class AsyncFilesResourceWithStreamingResponse:
    def __init__(self, files: AsyncFilesResource) -> None:
        self._files = files

        self.create = async_to_streamed_response_wrapper(
            files.create,
        )
        self.list = async_to_streamed_response_wrapper(
            files.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            files.delete,
        )
        self.complete = async_to_streamed_response_wrapper(
            files.complete,
        )
        self.get = async_to_streamed_response_wrapper(
            files.get,
        )

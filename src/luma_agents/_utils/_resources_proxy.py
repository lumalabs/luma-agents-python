from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `luma_agents.resources` module.

    This is used so that we can lazily import `luma_agents.resources` only when
    needed *and* so that users can just import `luma_agents` and reference `luma_agents.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("luma_agents.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()

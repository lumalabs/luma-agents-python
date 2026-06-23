# Generations

Types:

```python
from luma_agents.types import (
    AdvancedControls,
    DepthControl,
    FaceControl,
    Generation,
    GenerationFailureCode,
    GenerationOutput,
    ImageRef,
    Model,
    NormalsControl,
    PoseControl,
    PoseControlStrength,
    SourcePosition,
    TrajectoryControl,
    VideoDuration,
    VideoEditOptions,
    VideoEditStrength,
    VideoOptions,
    VideoResolution,
)
```

Methods:

- <code title="post /generations">client.generations.<a href="./src/luma_agents/resources/generations.py">create</a>(\*\*<a href="src/luma_agents/types/generation_create_params.py">params</a>) -> <a href="./src/luma_agents/types/generation.py">Generation</a></code>
- <code title="get /generations/{generation_id}">client.generations.<a href="./src/luma_agents/resources/generations.py">get</a>(generation_id) -> <a href="./src/luma_agents/types/generation.py">Generation</a></code>

# Files

Types:

```python
from luma_agents.types import (
    CreateFileResponse,
    File,
    FileList,
    FilePurpose,
    FileState,
    PresignedUpload,
)
```

Methods:

- <code title="post /files">client.files.<a href="./src/luma_agents/resources/files.py">create</a>(\*\*<a href="src/luma_agents/types/file_create_params.py">params</a>) -> <a href="./src/luma_agents/types/create_file_response.py">CreateFileResponse</a></code>
- <code title="get /files">client.files.<a href="./src/luma_agents/resources/files.py">list</a>(\*\*<a href="src/luma_agents/types/file_list_params.py">params</a>) -> <a href="./src/luma_agents/types/file_list.py">FileList</a></code>
- <code title="delete /files/{file_id}">client.files.<a href="./src/luma_agents/resources/files.py">delete</a>(file_id) -> None</code>
- <code title="post /files/{file_id}/complete">client.files.<a href="./src/luma_agents/resources/files.py">complete</a>(file_id) -> <a href="./src/luma_agents/types/file.py">File</a></code>
- <code title="get /files/{file_id}">client.files.<a href="./src/luma_agents/resources/files.py">get</a>(file_id) -> <a href="./src/luma_agents/types/file.py">File</a></code>

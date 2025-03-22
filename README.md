```bash
$ uv venv .venv

$ uv pip install -r pyproject.toml
```

```bash
$ uv add "mcp[cli]"
```

```bash
$ mcp dev src/echo_server.py
```

```text
http://localhost:5173
```

```bash
$ docker image build -t mcp/seminar .
```

```json
{
  "mcpServers": {
    "seminar_attendees": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "-p",
        "3010:3000",
        "mcp/seminar"
      ]
    }
  }
}
```

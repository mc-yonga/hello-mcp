# MCP Server 예제 : 세미나 관리 Agent

## 의존성 설치

```bash
$ uv venv .venv 

$ uv pip install -r pyproject.toml
```

## Docker image

```bash
$ docker image build -t mcp/seminar .
```

## MCP 클라이언트 설정

### Claude Desktop

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

### Cursor

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

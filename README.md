
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

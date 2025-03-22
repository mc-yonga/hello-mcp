from mcp.server.fastmcp import FastMCP

from semina import seminar_attendees

app = FastMCP("Echo")


@app.resource("echo://{message}")
def echo_resource(message: str) -> str:
    """Echo a message as a resource"""
    return f"Resource echo: {message}"


@app.resource("seminar://attendees")
def echo_resource() -> str:
    return seminar_attendees()


@app.tool()
def echo_tool(message: str) -> str:
    """Echo a message as a tool"""
    return f"Tool echo: {message}"


@app.prompt()
def echo_prompt(message: str) -> str:
    """Create an echo prompt"""
    return f"Please process this message: {message}"


if __name__ == "__main__":
    app.run()

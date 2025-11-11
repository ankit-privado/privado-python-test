from fastMCP import MCPClient
import json

def setup_mcp_connection():
    firstName = "name"
    mcp_base_url = "hello"
    client = MCPClient("python -m mcp_server_filesystem /path/to/directory", mcp_base_url)
    tools = client.listTools(firstName)  # <<<==== This is our expected detection
    print(json.dumps(tools, indent=2))
    return tools

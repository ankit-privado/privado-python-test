from anyai import MCPClient
import json

def setup_mcp_connection():
    firstName = "name"
    client = MCPClient("python -m mcp_server_filesystem /path/to/directory")
    tools = client.listTools(firstName)  # <<<==== This is our expected detection
    print(json.dumps(tools, indent=2))
    return tools

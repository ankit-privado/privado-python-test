from anyai import MCPClient
import json

def setup_mcp_connection():
    mcp_server_url = "www.mcpServer.com"
    client = MCPClient("python -m mcp_server_filesystem /path/to/directory", mcp_server_url)
    tools = client.listTools()  # <<<==== This is our expected detection
    print(json.dumps(tools, indent=2))
    return tools

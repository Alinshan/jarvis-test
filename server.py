from mcp.server.fastmcp import FastMCP
from starlette.responses import HTMLResponse

# make server
mcp = FastMCP("Jarvis")

@mcp.tool()
def hello():
    return "sir"

# simple page
html = "<html><body><h1>Jarvis Online</h1></body></html>"

async def root(request):
    return HTMLResponse(html)

def main():
    mcp.run()

if __name__ == "__main__":
    main()
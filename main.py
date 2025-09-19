from fastapi import FastAPI, Request, Depends
from mcp.server.sse import SseServerTransport
from starlette.routing import Mount
from animals import mcp
import uvicorn
from dotenv import load_dotenv

load_dotenv()


app = FastAPI(title="animals",lifespan=lambda app: mcp.session_manager.run())
app.mount("/", mcp.streamable_http_app())

if __name__ == "__main__":
    # used argparse to get the host and port parameters in args
    uvicorn.run(app,  host="0.0.0.0", port=8000,log_level="info")
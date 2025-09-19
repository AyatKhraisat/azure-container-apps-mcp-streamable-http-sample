import os
from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP
import logging
import json
# Initialize FastMCP server
mcp = FastMCP("animals")

# Constants
NWS_API_BASE = "https://api.api-ninjas.com/v1/animals"
 
async def make_request(url: str) -> dict[str, Any] | None:
    """Make a request to the ninjas API with proper error handling."""
    api_key = os.getenv("API_KEY" )
    headers = {
        "Accept": "application/json",
        "X-Api-Key": api_key
    }
    logging.basicConfig(
        format="%(levelname)s [%(asctime)s] %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except Exception:
            return Exception
         
@mcp.tool()
async def get_animal_infromation(name: str) -> str:
    """Get information about animal by name.

    Args:
        state: full animaal name (e.g., "Lion")
    """
    url = f"{NWS_API_BASE}?name={name}"
    data = await make_request(url)

    if not data  :
        return "Unable to fetch {name} information at this time."
  
    return    json.dumps(data)

@mcp.prompt( 
    name="write_article",          # Custom prompt name
    description="Creates article about an animal",  # Custom description
)
def write_article(animal: str) -> str:
    return f"""
get infromations about {animal}
after that use this informatino to Write a detailed, well-structured article about {animal}. The article should be engaging, informative, and easy to read. 

Make the tone informative yet friendly, suitable for a general audience, and around 200 words long
"""


@mcp.resource("file://dogs.txt", mime_type="text/plain")
async def read_dog() -> str:
    """Reads content from a specific   file asynchronously."""
    try:
            with open('dogs.txt', 'r') as file:
              content = file.read()  # Read the entire content of the file
            return content
    except FileNotFoundError:
        return "file not found."
    
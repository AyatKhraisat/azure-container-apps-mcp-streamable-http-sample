# Azure Container Apps MCP Streamable HTTP Sample

A sample implementation of a Model Context Protocol (MCP) server for Azure Container Apps management, demonstrating HTTP streamable responses. Built with Python, UV package manager, and Ninja API framework to showcase real-time container operations.


## Prerequisites

- Python 3.11+
- [UV](https://github.com/astral-sh/uv) package manager
- Azure subscription and Container Apps environment
- Azure CLI 

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/AyatKhraisat/azure-container-apps-mcp-streamable-http-sample.git
cd azure-container-apps-mcp-streamable-http-sample
```

### 2. Install dependencies with UV

```bash
# Install UV if you haven't already
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create virtual environment and install dependencies
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv sync
```

### 3. Environment Configuration

Create a `.env` file in the project root:

```env
# NINJA API KEY API_KEY 
API_KEY=<NINJA-API-KEY>
```

## Available Tools & Resources

### 🔧 Tools

#### `get_animal_infromation`
Retrieves comprehensive information about any animal.

**Parameters:**
- `name` (string): Full animal name (e.g., "Lion", "African Elephant", "Great White Shark")


**Sample Response:**
```json
[
  {
    "name": "Lion",
    "taxonomy": {
      "kingdom": "Animalia",
      "phylum": "Chordata",
      "class": "Mammalia",
      "order": "Carnivora",
      "family": "Felidae"
    },
    "locations": ["Africa", "India"],
    "characteristics": {
      "prey": "Antelope, Warthog, Crocodile",
      "predators": "Human",
      "lifestyle": "Pack",
      "diet": "Carnivore"
    }
  }
]
```

### 📋 Prompts

#### `write_article`
Generates structured prompts for creating informative animal articles.

**Parameters:**
- `animal` (string): Name of the animal to write about

**Returns:** A detailed prompt template that guides content creation



### 📚 Resources

#### `file://dogs.txt`
Provides access to local dog information stored in text files.

**MIME Type:** `text/plain`

## API Integration

### API Ninjas Animals Endpoint

The server integrates with the API Ninjas Animals API:

**Base URL:** `https://api-ninjas.com/api/animals`

**Authentication:** Requires `X-Api-Key` header



### Test Locally


```bash
uv run fastapi dev main.py
```
MCP Server: http://127.0.0.1:8000/mcp

## Deploy to Azure:
```bash

az containerapp up -g <RESOURCE_GROUP_NAME> -n animals-mcp --environment mcp -l <REGION> --env-vars API_KEYS=<NINJA_API_KEY> --source .
```


## Resources

- 📖 [Azure Container Apps Documentation](https://docs.microsoft.com/en-us/azure/container-apps/)
- 🔧 [Model Context Protocol Specification](https://modelcontextprotocol.io/)
- 🐍 [UV Documentation](https://docs.astral.sh/uv/)
- ⚡ [Ninja API Documentation](https://api-ninjas.com/api/animals)




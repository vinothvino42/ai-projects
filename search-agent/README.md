# Search Agent

Search Agent is a Python project that uses AI to search for and retrieve the top Flutter packages from pub.dev, including their descriptions and like counts. It leverages LangChain, OpenAI, and TavilySearch to provide structured, automated search results for Flutter developers.

## Features

- Retrieves the top 5 most liked Flutter packages from pub.dev
- Provides package name, description, and number of likes
- Utilizes AI-powered search, tool calling (function calling), and structured response parsing
- Easily extensible for other search queries or data sources

## Requirements

- Python 3.14+
- [Ollama](https://ollama.com/) (if using local models)
- OpenAI API key
- TavilySearch API key

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/vinothvino42/ai-projects.git
   cd search-agent
   ```
2. Install [uv](https://github.com/astral-sh/uv) if you don't have it:
   ```bash
   pip install uv
   ```
3. Install dependencies using uv:
   ```bash
   uv venv && uv add -r requirements.txt
   ```
4. Setup environment variables:
   ```bash
   cp .env.example .env
   # Then edit .env to add your API keys
   ```

## Usage

Run the main script to fetch and display the top Flutter packages:

```bash
python main.py
```

The script will output the top 5 most liked Flutter packages, along with their descriptions and like counts, directly to the console.

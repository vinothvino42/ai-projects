# Hello World: LangChain AI Summary Project

This project demonstrates a simple use of [LangChain](https://python.langchain.com/) to generate a summary and interesting facts about a person using AI language models. It leverages both OpenAI and Ollama models, and is designed as a starting point for experimenting with prompt engineering and LLM chains in Python.

## Features

- Loads environment variables from `.env` (see `.env.example`)
- Uses LangChain's prompt templates, LLM chains, and tool calling (function calling)
- Supports both OpenAI and Ollama models (default: Ollama's `gemma4`)
- Summarizes information and generates interesting facts

## Requirements

- Python 3.14+
- OpenAI API key
- [Ollama](https://ollama.com/) (if using local models)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/vinothvino42/ai-projects.git
   cd hello-world
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

Run the main script:

```bash
python main.py
```

You should see a summary and two interesting facts about Elon Musk printed to the console.

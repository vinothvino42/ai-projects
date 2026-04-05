# Hello World: LangChain AI Summary Project

This project demonstrates a simple use of [LangChain](https://python.langchain.com/) to generate a summary and interesting facts about a person using AI language models. It leverages both OpenAI and Ollama models, and is designed as a starting point for experimenting with prompt engineering and LLM chains in Python.

## Features

- Loads environment variables from `.env` (see `.env.example`)
- Uses LangChain's prompt templates and LLM chains
- Supports both OpenAI and Ollama models (default: Ollama's `gemma4`)
- Summarizes information and generates interesting facts

## Requirements

- Python 3.14+
- [Ollama](https://ollama.com/) (if using local models)
- OpenAI API key (if using OpenAI models)

Install dependencies:

```bash
pip install -r requirements.txt
```

## Setup

1. Copy `.env.example` to `.env` and add your OpenAI API key if using OpenAI models.
2. (Optional) Install and run Ollama for local LLM support.

## Usage

Run the main script:

```bash
python main.py
```

You should see a summary and two interesting facts about Elon Musk printed to the console.

## Customization

- To use a different model, modify the `llm` assignment in `main.py`.
- To summarize different information, change the `information` variable.

## License

This project is licensed under the MIT License.

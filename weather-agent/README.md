# Weather Agent

Weather Agent provides current weather information for any city using AI-powered agents and the OpenWeatherMap API. It leverages LangChain, OpenAI, and a tool-calling mechanism to fetch real-time weather data. This project demonstrates how to build an AI-powered agent that can answer user queries using external APIs.

## Features

- Provides current weather information for any city worldwide
- Uses OpenWeatherMap API for real-time weather data
- AI-powered agent with tool-calling (function calling)
- Easily extensible for more features or APIs

## Requirements

- Python 3.14+
- [Ollama](https://ollama.com/) (if using local models)
- OpenAI API key (for LLM)
- OpenWeatherMap API key

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/vinothvino42/ai-projects.git
   cd weather-agent
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
   - Create a `.env` file and add your API keys:
     ```env
     OPENAI_API_KEY=your_openai_api_key
     OPENWEATHER_API_KEY=your_openweathermap_api_key
     ```

## Usage

Run the main script to get the weather for a city:

```bash
python main.py
```

By default, the script will ask for the weather in Trivandrum using the OpenWeatherMap API. You can modify the code to query other cities or extend the tool for more dynamic input.

The script will output the current weather for the requested city directly to the console, e.g.:

## Example Output

```
Clear sky, 34°C
```

## Extending

- To add more features (e.g., forecast, humidity), update the `get_weather` tool in `main.py`.
- You can further customize the agent or integrate with other APIs as needed.

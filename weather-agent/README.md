# Weather Agent

Weather Agent provides current weather information for a given city using AI-powered agents and tool-calling. It leverages LangChain, OpenAI, and a simple tool-calling mechanism to return weather data for select cities. This project demonstrates how to build an AI-powered agent that can answer user queries using structured tools.

## Features

- Provides current weather information for select cities (Chennai, Bangalore, Mumbai)
- Uses AI-powered agent with tool-calling (function calling)
- Easily extensible to support more cities or integrate real weather APIs

## Requirements

- Python 3.14+
- [Ollama](https://ollama.com/) (if using local models)
- OpenAI API key

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
   - Create a `.env` file and add your OpenAI API key:
     ```env
     OPENAI_API_KEY=your_openai_api_key
     ```

## Usage

Run the main script to get the weather for a city:

```bash
python main.py
```

By default, the script will ask for the weather in Chennai. You can modify the code to query other cities or extend the tool for more dynamic input.

The script will output the current weather for the requested city directly to the console.

## Example Output

```
Weather data for Chennai: Sunny, 34°C
```

## Extending

- To add more cities, update the `weather_data` dictionary in `main.py`.
- To use real weather data, replace the `get_weather` tool implementation with an API call to a weather service.

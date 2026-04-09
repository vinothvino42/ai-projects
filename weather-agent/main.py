import os

import requests
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool

load_dotenv()

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")


@tool
def get_weather(city: str) -> str:
    """Get current weather for a city using OpenWeatherMap API."""

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric",
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        if response.status_code != 200:
            return f"Error: {data.get('message', 'Unable to fetch weather')}"

        weather = data["weather"][0]["description"].capitalize()
        temp = data["main"]["temp"]

        return f"{weather}, {temp}°C"

    except Exception as e:
        return f"Error fetching weather: {str(e)}"


agent = create_agent(
    model="gpt-5.4-mini",
    tools=[get_weather],
    system_prompt="You are a helpful assistant that provides weather information.",
)

response = agent.invoke(
    {"messages": [{"role": "user", "content": "What's the weather in Trivandrum today?"}]}
)

print(response["messages"][-1].content)

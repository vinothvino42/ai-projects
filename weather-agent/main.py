from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool

load_dotenv()


@tool
def get_weather(city: str) -> str:
    """Get current weather for a city."""

    weather_data = {
        "chennai": "Sunny, 34°C",
        "bangalore": "Cloudy, 25°C",
        "mumbai": "Humid, 30°C",
    }

    return weather_data.get(city.lower(), "Weather data not available")


agent = create_agent(
    model="gpt-4o-mini",
    tools=[get_weather],
    system_prompt="You are a helpful assistant that provides weather information.",
)

response = agent.invoke(
    {"messages": [{"role": "user", "content": "What's the weather in Chennai today?"}]}
)

print(response["messages"][-1].content)

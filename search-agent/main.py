from typing import List

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from pydantic import BaseModel, Field

load_dotenv()


class Package(BaseModel):
    name: str = Field(description="Package name")
    description: str = Field(description="Short description")
    likes: int = Field(description="Number of likes")


class FlutterPackages(BaseModel):
    packages: List[Package]


tavily_tool = TavilySearch(max_results=5)
llm = ChatOpenAI(model="gpt-4o", temperature=0)
agent = create_agent(model=llm, tools=[tavily_tool], response_format=FlutterPackages)


def main():
    query = "Top 5 most liked Flutter packages on pub.dev with description and likes"
    response = agent.invoke({"messages": [HumanMessage(content=query)]})
    result: FlutterPackages = response["structured_response"]

    for pkg in result.packages:
        print(
            f"\n\nTitle: {pkg.name}\nDescription: {pkg.description}\nLikes: {pkg.likes}"
        )


if __name__ == "__main__":
    main()

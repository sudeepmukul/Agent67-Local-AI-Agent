from langchain_core.tools import tool
from tavily import TavilyClient
from config import TAVILY_API_KEY
client = TavilyClient(api_key=TAVILY_API_KEY)
@tool
def web_search(query: str) -> str:
    """Search the web for recent and factual information."""
    response = client.search(query=query, search_depth="advanced", max_results=5)
    print("Search Finished")
    output = []

    for result in response["results"]:
        output.append(
            f"""
Title: {result['title']}

Content:
{result['content']}

URL:
{result['url']}
"""
        )

    return "\n\n".join(output)
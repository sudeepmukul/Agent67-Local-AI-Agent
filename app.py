from llm import llm
from agent.graph import graph
from langchain_core.messages import HumanMessage
while True:
    query = input("Unc: ")

    if query.lower()=="fkoff":
        break
    result = graph.invoke(
        {
            "messages":[
                HumanMessage(query)
            ]
        }
    )
    print("Agent 67: ", result["messages"][-1].content)
    print()

from llm import llm

def chatbot(state):
    response = llm.invoke(state["messages"])

    print("\nTool Calls:", response.tool_calls)

    return {
        "messages": [response]
    }
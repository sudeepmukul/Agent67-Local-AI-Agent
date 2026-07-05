from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode
from .state import State
from .nodes import chatbot
from tools import TOOLS
from langgraph.prebuilt import tools_condition

builder = StateGraph(State)
builder.add_node("chatbot", chatbot)
builder.add_node("tools", ToolNode(TOOLS))
builder.add_edge(START, "chatbot")

builder.add_conditional_edges(
    "chatbot",
    tools_condition,
)

builder.add_edge("tools", "chatbot")

graph = builder.compile()

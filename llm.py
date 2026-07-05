from langchain_ollama import ChatOllama
from config import MODEL_NAME, TEMPERATURE
from tools import TOOLS
llm = ChatOllama(
    model=MODEL_NAME,
    temperature=TEMPERATURE,
).bind_tools(TOOLS)


from datetime import datetime
from langchain_core.tools import tool

@tool
def get_current_time()-> str:
    """Return the current date and time."""
    return datetime.now().strftime("%d %B %Y %I:%M:%S %p")
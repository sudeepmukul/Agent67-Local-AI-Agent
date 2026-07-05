from dotenv import load_dotenv
load_dotenv()
import os
MODEL_NAME = "qwen3:8b"

TEMPERATURE = 0.7
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
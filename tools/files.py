from pathlib import Path
from langchain_core.tools import tool


@tool
def write_file(
    content: str,
    filename: str = "output.txt"
) -> str:
    """
    Save text content to a file.
    IMPORTANT:
    Only call this tool after you already have the final content.
    Never use placeholders like:
    [Insert content here]
    Args:
        content: The text to save.
        filename: Name of the file including extension.
    """

    try:
        path = Path(filename)

        # create parent folders if needed
        path.parent.mkdir(parents=True, exist_ok=True)

        path.write_text(
            content,
            encoding="utf-8"
        )

        return f"Saved successfully to {path.resolve()}"

    except Exception as e:
        return f"Error saving file: {str(e)}"
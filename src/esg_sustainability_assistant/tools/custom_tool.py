from typing import Type

from crewai.tools import BaseTool
from pydantic import BaseModel, Field


class MyCustomToolInput(BaseModel):
    """
    Input schema for ``MyCustomTool``.

    Parameters
    ----------
    argument : str
        A single input string argument used by the tool.
    """

    argument: str = Field(..., description="Description of the argument.")


class MyCustomTool(BaseTool):
    """
    Example CrewAI tool with a minimal interface.

    Notes
    -----
    Replace this example with your production implementation. The current
    ``_run`` method returns a static string.
    """

    name: str = "Name of my tool"
    description: str = (
        "Clear description for what this tool is useful for, your agent will need this information to use it."
    )
    args_schema: Type[BaseModel] = MyCustomToolInput

    def _run(self, argument: str) -> str:
        """
        Execute the tool.

        Parameters
        ----------
        argument : str
            Input argument used by the tool.

        Returns
        -------
        str
            A simple example output string.
        """
        return "this is an example of a tool output, ignore it and move along."

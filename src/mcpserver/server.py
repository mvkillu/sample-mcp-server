from mcp.server.fastmcp import FastMCP
import random

mcp = FastMCP("random-number")


@mcp.tool()
def get_random_number(limit: int) -> int:
    """Generate a random number between 1 and the upper limit provided by the user

    Returns:
        int: A random number between 1 and the upper limit provided by user
    """
    return random.randint(1, limit)

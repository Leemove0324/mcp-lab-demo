from mcp.server.fastmcp import FastMCP

mcp = FastMCP("campus-tools")


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two integers."""
    return a + b


@mcp.tool()
def grade_message(score: int) -> str:
    """Return a simple grade message from a score."""
    if score >= 90:
        return "A: excellent"
    if score >= 80:
        return "B: good"
    if score >= 70:
        return "C: keep practicing"
    return "Needs more practice"


@mcp.tool()
def campus_notice(keyword: str) -> str:
    """Find a sample campus notice by keyword: exam or project."""
    notices = {"exam": "Midterm: Week 8", "project": "Team demo: Week 14"}
    return notices.get(keyword.lower(), "No matching notice")


if __name__ == "__main__":
    mcp.run(transport="stdio")

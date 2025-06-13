"""Top-level package for the Sefaria FastMCP server.

The :data:`mcp` object is the fully configured FastMCP server instance so
external code (tests, other servers, etc.) can import it directly:

    from sefaria_mcp import mcp

For CLI usage, install the package and run the `sefaria-mcp` command that is
declared in *pyproject.toml* – it simply calls :pyfunc:`.main`.
"""

from .main import mcp, main  # re-export for convenience

__all__: list[str] = ["mcp", "main"] 
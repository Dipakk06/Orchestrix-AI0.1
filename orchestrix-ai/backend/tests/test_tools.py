from app.tools.registry import ToolRegistry


def test_calculator_tool():
    registry = ToolRegistry()
    out = registry.run("calculator", {"expression": "3 * (2 + 1)"})
    assert out["result"] == 9


def test_web_search_placeholder():
    registry = ToolRegistry()
    out = registry.run("web_search", {"query": "latest AI news"})
    assert out["status"] == "placeholder"

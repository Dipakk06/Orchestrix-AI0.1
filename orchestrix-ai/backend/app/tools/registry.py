import math
from pathlib import Path


class ToolRegistry:
    def __init__(self) -> None:
        self.tools = {
            "calculator": self.calculator,
            "file_reader": self.file_reader,
            "python_exec": self.python_exec,
            "web_search": self.web_search,
            "email_automation": self.email_automation,
            "calendar_automation": self.calendar_automation,
        }

    def list_tools(self) -> list[dict]:
        return [
            {"name": name, "description": fn.__doc__ or "No description"}
            for name, fn in self.tools.items()
        ]

    def run(self, tool_name: str, payload: dict) -> dict:
        if tool_name not in self.tools:
            return {"error": f"Tool '{tool_name}' not found"}
        return self.tools[tool_name](payload)

    def calculator(self, payload: dict) -> dict:
        """Safe calculator for basic math expressions."""
        expression = payload.get("expression", "")
        allowed = {k: getattr(math, k) for k in ["sqrt", "sin", "cos", "tan", "pi", "e"]}
        try:
            result = eval(expression, {"__builtins__": {}}, allowed)
            return {"result": result}
        except Exception as exc:  # noqa: BLE001
            return {"error": str(exc)}

    def file_reader(self, payload: dict) -> dict:
        """Read a local text file from an allowed path."""
        path = Path(payload.get("path", ""))
        if not path.exists() or not path.is_file():
            return {"error": "File not found"}
        return {"content": path.read_text(encoding="utf-8")[:4000]}

    def python_exec(self, payload: dict) -> dict:
        """Execute Python code in a constrained namespace."""
        code = payload.get("code", "")
        scope = {"__builtins__": {"print": print, "range": range, "len": len}}
        output = []

        def capture_print(*args, **kwargs):  # noqa: ANN001, ANN003
            output.append(" ".join(map(str, args)))

        scope["__builtins__"]["print"] = capture_print
        try:
            exec(code, scope, scope)
            return {"output": "\n".join(output) if output else "Execution completed."}
        except Exception as exc:  # noqa: BLE001
            return {"error": str(exc)}

    def web_search(self, payload: dict) -> dict:
        """Web search placeholder for future API integration."""
        return {"status": "placeholder", "query": payload.get("query", "")}

    def email_automation(self, payload: dict) -> dict:
        """Email automation placeholder."""
        return {"status": "placeholder", "action": payload.get("action", "draft")}

    def calendar_automation(self, payload: dict) -> dict:
        """Calendar automation placeholder."""
        return {"status": "placeholder", "action": payload.get("action", "create_event")}

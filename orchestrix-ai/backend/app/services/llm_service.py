import json
import logging

import ollama

from app.core.config import get_settings

logger = logging.getLogger(__name__)
settings = get_settings()
client = ollama.Client(host=settings.ollama_base_url)


def generate_response(prompt: str, history: list[dict] | None = None) -> str:
    messages = history or []
    messages.append({"role": "user", "content": prompt})
    response = client.chat(model=settings.ollama_model, messages=messages)
    return response["message"]["content"]


def stream_response(prompt: str, history: list[dict] | None = None):
    messages = history or []
    messages.append({"role": "user", "content": prompt})
    for chunk in client.chat(model=settings.ollama_model, messages=messages, stream=True):
        content = chunk.get("message", {}).get("content")
        if content:
            yield f"data: {json.dumps({'token': content})}\n\n"
    yield "data: [DONE]\n\n"

import tempfile
from pathlib import Path

import pyttsx3
import whisper

from app.core.config import get_settings

settings = get_settings()
_whisper_model = whisper.load_model(settings.whisper_model)


def speech_to_text(audio_bytes: bytes) -> str:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(audio_bytes)
        tmp_path = Path(tmp.name)
    result = _whisper_model.transcribe(str(tmp_path))
    tmp_path.unlink(missing_ok=True)
    return result.get("text", "")


def text_to_speech(text: str) -> str:
    engine = pyttsx3.init()
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
        out_path = Path(tmp.name)
    engine.save_to_file(text, str(out_path))
    engine.runAndWait()
    return str(out_path)

from fastapi import APIRouter, File, UploadFile
from fastapi.responses import FileResponse

from app.schemas.voice import TTSRequest, TTSResponse
from app.services.voice_service import speech_to_text, text_to_speech

router = APIRouter(prefix="/api", tags=["voice"])


@router.post("/voice/stt")
async def stt(audio: UploadFile = File(...)):
    data = await audio.read()
    text = speech_to_text(data)
    return {"text": text}


@router.post("/voice/tts", response_model=TTSResponse)
def tts(payload: TTSRequest):
    path = text_to_speech(payload.text)
    return TTSResponse(status="ok", message=path)


@router.post("/voice/tts/file")
def tts_file(payload: TTSRequest):
    path = text_to_speech(payload.text)
    return FileResponse(path, media_type="audio/mpeg", filename="orchestrix-response.mp3")

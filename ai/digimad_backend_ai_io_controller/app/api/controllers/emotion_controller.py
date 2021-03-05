from fastapi import APIRouter, HTTPException, Response
from app.infrastructure.mock.emotion_repository import EmotionRepository
from app.infrastructure.mock.emotion_lab_repository import EmotionLabRepository
from app.domain.models.emotion import Emotion
from app.domain.models.InputEmotion import InputEmotion

from colorutils import hex_to_hsv
import requests
import json


router = APIRouter()


@router.get('/api/emotions/{emotion_name}')
def get_emotion_by_id(emotion_name: str):
    emotion = EmotionRepository().get_by_id(emotion_name)
    if emotion is None:
        raise HTTPException(status_code=404, detail="emotion not found")

    return emotion


@router.get("/api/emotions")
def get_emotions():
    return EmotionRepository().get_all()

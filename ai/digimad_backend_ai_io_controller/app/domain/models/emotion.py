from pydantic import BaseModel
from enum import Enum


class Emotion(BaseModel):
    emotion_name: str


class EmotionEnum(Enum):
    ANGRY = 1
    DISGUST = 2
    SCARED = 3
    HAPPY = 4
    SAD = 5
    SURPRISED = 6
    NEUTRAL = 7

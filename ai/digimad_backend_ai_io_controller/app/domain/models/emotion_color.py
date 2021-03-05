from pydantic import BaseModel


class EmotionColor(BaseModel):
    emotion_name: str
    nth_color: int
    color_name: str

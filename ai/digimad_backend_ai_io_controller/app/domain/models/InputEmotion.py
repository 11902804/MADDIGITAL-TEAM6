from pydantic import BaseModel


class InputEmotion(BaseModel):
    emotion: str
    wid: int

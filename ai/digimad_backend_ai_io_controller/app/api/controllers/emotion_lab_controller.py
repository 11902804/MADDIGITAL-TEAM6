from fastapi import APIRouter, HTTPException, Response
from app.infrastructure.mock.emotion_lab_repository \
     import EmotionLabRepository
from app.domain.models.emotion_color import EmotionColor


router = APIRouter()


@router.get('/api/emotionlab/{emotion_name}')
def get_emotion_color_by_id(emotion_name: str):
    emotion_color = EmotionLabRepository() \
                      .get_by_id(emotion_name)
    if emotion_color is None:
        raise HTTPException(status_code=404,
                            detail="emotion_color not found")

    return emotion_color


@router.get("/api/emotionlab")
def get_all_emotion_colors():
    emotion_colors = EmotionLabRepository().get_all()

    if emotion_colors is None:
        raise HTTPException(status_code=404,
                            detail="No emotion_colors in lab")

    return emotion_colors


@router.put('/api/emotionlab/', status_code=202)
def update_emotion_color(emotion_color: EmotionColor):
    emotion_color = EmotionLabRepository() \
                      .update(emotion_color.emotion_name,
                              emotion_color.nth_color,
                              emotion_color.color_name)
    if emotion_color is None:
        raise HTTPException(status_code=404,
                            detail="emotion_color not found")

    return emotion_color

from app.domain.models.edit_color_name import EditColorName
from fastapi import APIRouter, HTTPException, Response
from app.infrastructure.mock.color_repository import ColorRepository
from app.domain.models.color import Color


router = APIRouter()


@router.get('/api/colors/{color_name}')
def get_color(color_name: str):
    color = ColorRepository().get_by_name(color_name)
    if color is None:
        raise HTTPException(status_code=404, detail="Color not found")

    return color


@router.post('/api/colors')
def insert_color_request(color: Color):
    return ColorRepository().create(color.color_name, color.hex_value)


@router.get("/api/colors")
def get_predefined_colors_request():
    colors = ColorRepository().get_all()

    if colors is None:
        raise HTTPException(status_code=404, detail="No colors in database")

    return colors


@router.put('/api/colors', status_code=202)
def update_colorName(edit_color_name: EditColorName):
    updated_color = ColorRepository().update(edit_color_name.old_name, edit_color_name.new_name)
    if edit_color_name.old_name is None:
        raise HTTPException(status_code=404, detail="Color not found")
 
    return updated_color


@router.delete('/api/colors/{color_name}', status_code=204, response_class=Response)
def delete_color(color_name: str):
    deleted = ColorRepository().delete(color_name)
    if deleted is None:
        raise HTTPException(status_code=404, detail="Color not found")

    return

from pydantic import BaseModel


class EditColorName(BaseModel):
    old_name: str
    new_name: str


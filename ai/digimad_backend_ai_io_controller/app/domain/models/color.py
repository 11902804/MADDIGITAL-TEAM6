from pydantic import BaseModel


class Color(BaseModel):
    color_name: str
    hex_value: str

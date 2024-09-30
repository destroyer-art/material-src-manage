from pydantic import BaseModel


class PreferenceModel(BaseModel):
    material: str
    form: str
    grade: str
    choice: str
    min_width: str
    max_width: str
    min_thickness: str
    max_thickness: str

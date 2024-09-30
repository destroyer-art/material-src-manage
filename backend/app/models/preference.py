from pydantic import BaseModel


class PreferenceModel(BaseModel):
    material: str
    form: str
    grade: str
    choice: str
    min_width: float
    max_width: float
    min_thickness: float
    max_thickness: float

from sqlalchemy import Column, String, Numeric

from database.dbconnect import Base


class PreferenceSchema(Base):
    __tablename__ = "Preference"

    ID = Column(String, primary_key=True)

    material = Column(String, nullable=False)
    form = Column(String, nullable=False)
    grade = Column(String, nullable=True)
    choice = Column(String, nullable=True)
    min_width = Column(Numeric, nullable=True)
    max_width = Column(Numeric, nullable=True)
    min_thickness = Column(Numeric, nullable=True)
    max_thickness = Column(Numeric, nullable=True)

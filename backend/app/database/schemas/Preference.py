from app import dbHandler


class PreferenceSchema(dbHandler.Model):
    __tablename__ = "Preference"

    ID = dbHandler.Column(dbHandler.String(128), primary_key=True)
    material = dbHandler.Column(dbHandler.String(128), nullable=False)
    form = dbHandler.Column(dbHandler.String(128), nullable=False)
    grade = dbHandler.Column(dbHandler.String(128), nullable=True)
    choice = dbHandler.Column(dbHandler.String(128), nullable=True)
    min_width = dbHandler.Column(dbHandler.Integer, nullable=True)
    max_width = dbHandler.Column(dbHandler.Integer, nullable=True)
    min_thickness = dbHandler.Column(dbHandler.Integer, nullable=True)
    max_thickness = dbHandler.Column(dbHandler.Integer, nullable=True)

from . import db

class Ingredient(db.Model):
    __tablename__ = 'Ingredients'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(200))
    crust = db.Column(db.Boolean, default=False, nullable=False)
    cheese = db.Column(db.Boolean, default=False, nullable=False)
    sauce = db.Column(db.Boolean, default=False, nullable=False)
    topping = db.Column(db.Boolean, default=False, nullable=True)
    file_path = db.Column(db.String(120), nullable=False)


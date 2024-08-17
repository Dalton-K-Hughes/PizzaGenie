from . import db

class BaseIngredient(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(200))
    file_path = db.Column(db.String(120))

class Crust(BaseIngredient):
    __tablename__ = 'crusts'

class Cheese(BaseIngredient):
    __tablename__ = 'cheeses'
    
class Sauce(BaseIngredient):
    __tablename__ = 'sauces'

class Topping(BaseIngredient):
    __tablename__ = 'toppings'
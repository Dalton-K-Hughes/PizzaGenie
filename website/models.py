from . import db

class Crust(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
class Cheese(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
class Sauce(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
class Toppings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
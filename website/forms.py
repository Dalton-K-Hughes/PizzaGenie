from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, FileField, SubmitField
from wtforms.validators import DataRequired

class AddToppingForm(FlaskForm):
    choices = [(1, 'Crust'), (2, 'Sauce'), (3, 'Cheese'), (4, 'Topping')]
    name = StringField('Name of Item', validators=[DataRequired()])
    description = StringField('Item Description', validators=[DataRequired])
    choices = SelectField('Crust, Sauce, Cheese, Topping?', choices=choices, validators=[DataRequired()])
    img = FileField('Image', validators=[DataRequired()], )
    submit = SubmitField('Add Item', validators=[DataRequired()])
from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    astronaut_id = StringField(
        "Id астронавта", validators=[DataRequired()])
    astronaut_pw = PasswordField(
        "Пароль астронавта", validators=[DataRequired()])
    captain_id = StringField("Id капитана", validators=[DataRequired()])
    captain_pw = PasswordField("Пароль капитана", validators=[DataRequired()])
    submit = SubmitField("Доступ")


class FileForm(FlaskForm):
    filename = FileField()
    submit = SubmitField("Отправить")

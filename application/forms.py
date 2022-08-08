from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField,DateField,URLField,DateTimeField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from application.models import User
import requests

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6, max=15)])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Login")


class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6, max=15)])
    password_confirm = PasswordField("Confirm Password",
                                     validators=[DataRequired(), Length(min=6, max=15), EqualTo('password')])
    first_name = StringField("First Name", validators=[DataRequired(), Length(min=2, max=55)])
    last_name = StringField("Last Name", validators=[DataRequired(), Length(min=2, max=55)])
    position = SelectField("Group Position", choices=[('member', 'member'), ('lead', 'group lead'), ('tutor', 'tutor')])
    submit = SubmitField("Register Now")

    def check_email_exist(self,email):
        url = "https://api.companyurlfinder.com/email-verification/"+email.data
        response = requests.request("GET", url).json()
        return str(response['response']['format'])

    def validate_email(self, email):
        email_exist = self.check_email_exist(email)
        if not email_exist:
            raise ValidationError("Email from invalid domain. Pick another one.")
        user = User.objects(email=email.data).first()
        if user:
            raise ValidationError("Email is already in use. Pick another one.")

class ADDNewTaskForm(FlaskForm):
    title = StringField("Task Title", validators=[DataRequired(), Length(min=2, max=120)])
    description = StringField("Description")
    phase = SelectField("Task Phases", choices=[('0', 'Not start yet'), ('1', 'Working on it'), ('2', 'Done'), ('3', 'Stuck'), ('4', 'Waiting'), ('5', 'Overdue')])
    deadline = DateField("Due Date")
    submit = SubmitField("Update Now")
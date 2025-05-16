from dataclasses import field
from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import  Email
from wtforms import validators

from app.models import User



class RegisterForm(FlaskForm):
    name = StringField('Name', [
                validators.DataRequired(),
                validators.Length(max=64)
                ])      
    username = StringField('Username', [
                validators.DataRequired(),
                validators.Length(max=64)
                ])
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username')
    email = EmailField('Email Address', [
                validators.DataRequired(),
                validators.Length(max=120),
                Email()
                ])
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address')
    password = PasswordField('Password', [
                validators.DataRequired(message='password is required'),
                validators.Length(message='password should be at least 8 char', min=8)
                ])
    password2 = PasswordField( 'Repeat Password', [
                validators.data_required(message='Confirm password'),
                validators.EqualTo('password', message='Passwords must match')
                
                                          ])
    register = SubmitField('Register')    
     
    
    
# class LoginForm(FlaskForm):
#     email = EmailField('Email Address', [
#                 validators.DataRequired(),
#                 Email()
#                 ])
#     password = PasswordField('Password', [
#                 validators.DataRequired(message='password is required'),
#                 ])
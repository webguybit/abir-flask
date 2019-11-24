# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 11:24:09 2019

@author: qxz0ga0
"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, \
    TextAreaField, SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, \
    Length
from app.models import User
from app.models import Device

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')


class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')




class DeviceRegistrationForm(FlaskForm):
    deviceId = StringField('Device ID', validators=[DataRequired()])
    devicename = StringField('Device Name', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    dept_code = StringField('Dept. Code', validators=[DataRequired()])
    device_function = StringField('Function', validators=[DataRequired()])
    device_bg=SelectField('Device Background', choices=[('bg1id', 'BG1'), ('bg2id', 'BG2'), ('bg3id', 'BG3')])
    # device_image = # HAVE TO LET USER UPLOAD IMAGE OF THE DEVICE
    # background_img = # HAVE TO LET USER SELECT WHICH IMAGE TO USE AS BACKGROUND FROM DROPDOWN LIST
    submit = SubmitField('Save')

    def validate_deviceId(self, deviceId):
        deviceid = Device.query.filter_by(deviceId=deviceId.data).first()
        if deviceid is not None:
            raise ValidationError('Please use a different Device ID.')
        

class DeviceEditForm(FlaskForm):
    # deviceId = StringField('Device ID', validators=[DataRequired()])
    devicename = StringField('Device Name', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    dept_code = StringField('Dept. Code', validators=[DataRequired()])
    device_function = StringField('Function', validators=[DataRequired()])
    device_bg=SelectField('Device Background', choices=[('bg1id', 'BG1'), ('bg2id', 'BG2'), ('bg3id', 'BG3')])
    # device_image = # HAVE TO LET USER UPLOAD IMAGE OF THE DEVICE
    # background_img = # HAVE TO LET USER SELECT WHICH IMAGE TO USE AS BACKGROUND FROM DROPDOWN LIST
    submit = SubmitField('Update')

    
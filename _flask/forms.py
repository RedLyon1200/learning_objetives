#!/usr/bin/env python3

from wtforms import Form
from wtforms import StringField, TextField
from wtforms.fields.html5 import EmailField
from wtforms import validators
from wtforms import HiddenField
from wtforms import PasswordField


def lenght_honeypot(form, field):
    if len(field.data) > 0:
        raise validators.ValidationError('Honeypot not empty')


class UserForm(Form):
    id = StringField('Id')
    username = StringField(
        'Username',
        [
            validators.Required(message='Username required!'),
            validators.length(min=4, max=20, message='Username not valid')
        ]
    )
    email = EmailField('Email')
    honeypot = HiddenField(
        '',
        [lenght_honeypot]
    )


class LoginForm(Form):
    username = StringField(
        'Username',
        [
            validators.Required(message='Username required!'),
            validators.length(min=4, max=20, message='Username not valid')
        ]
    )
    password = PasswordField(
        'Password',
        [validators.Required('Password is required')]
    )

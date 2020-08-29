#!/usr/bin/env python3
# -*- Copyright: Santiago Agudelo -*-
# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
from flask import render_template
from flask import make_response
from flask import session
from flask import redirect
from flask import url_for
from flask import flash
from uuid import uuid4

import forms
import json

app = Flask(__name__)
app.secret_key = str(uuid4())

app_id = str(uuid4())


@app.errorhandler(404)
def error_404_not_found(e):
    return render_template('404.html'), 404


@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        print('\n\n\n\n', username)
    custom_cookie = request.cookies.get('custom_cookie', 'Undefined')
    print('{}'.format(custom_cookie))
    return render_template('index.html', title='Santiago Agudelo')


@app.route('/hire/')
def id():
    return render_template('hire.html', title='Hire me', id=app_id)


@app.route('/projects/')
def projects():
    return render_template(
        'projects.html',
        title='Santiago Agudelo | Projects'
    )


@app.route('/form/', methods=['GET', 'POST'])
def form():
    user_form = forms.UserForm(request.form)
    if request.method == 'POST' and user_form.validate():
        print('OK')
    else:
        print('ERROR')
    return render_template('form.html', form=user_form, title='Form')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    login_form = forms.LoginForm(request.form)
    if request.method == 'POST' and login_form.validate():
        username = login_form.username.data
        logged_in = 'Logged in - {}'.format(username)
        session['username'] = username
        flash(logged_in)
    else:
        flash('Logged out')

    return render_template('login.html', form=login_form)


@app.route('/ajax-login/', methods=['POST'])
def ajax_login():
    print(request.form)
    username = request.form['username']
    response = {'status': 200, 'username': username, 'id': app_id}
    return json.dumps(response)


@app.route('/logout/')
def logout():
    if 'username' in session:
        session.pop('username')
    return redirect(url_for('login'))


@app.route('/cookie/')
def cookie():
    response = make_response(render_template(
        'cookie.html',
        id=app_id,
        title='Cookie'
    ))

    response.set_cookie('custom_cookie', app_id)
    return response


if __name__ == "__main__":
    app.run(debug=True, port=8000)


from flask import Blueprint,render_template, jsonify, request, session
from flask_login import login_user
from session import User
from users import users


login_page = Blueprint('login_page', __name__, template_folder='templates')


@login_page.get('/')
def show_login_page():
    return render_template('index.html')


@login_page.post('/login')
def login():
    data = request.get_json()

    username = data['username']

    session['key'] = username
    session['value'] = username

    user = User()
    user.id = username

    login_user(user)

    users[username] = {'username': username}

    return jsonify({'username': username})
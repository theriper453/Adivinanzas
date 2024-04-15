
from flask import Blueprint, render_template, jsonify, request
from flask_login import login_required
from matches import matches


match_page = Blueprint('match_page', __name__, template_folder='templates')


next_match_id = 565_452


@match_page.post('/create-match')
def create_match():
    data = request.get_json()

    username = data['username']

    matches[username] = {'username': username}

    return jsonify(matches[username])


@match_page.get('/join-match')
def join_match():
    data = request.get_json()

    username = data['username']

    matches[username] = {'username': username}

    return jsonify(matches[username])


@match_page.get('/match/<username>')
@login_required
def join_match(username):
    
    if username in matches:
        return render_template('match.html', username=username)
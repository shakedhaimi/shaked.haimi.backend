from flask import Flask, redirect, render_template, request, session, url_for, jsonify
import mysql.connector
import requests
import json
import collections

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello! How Can We Help?"


# -----Assignment 10------#
from assignment10.assignment10 import assignment10

app.register_blueprint(assignment10)


def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         password='shakedH121595',
                                         database='WEBHomework')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)

    if query_type == 'commit':
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value


# ----Assignment 8-----#
@app.route('/assignment8')
def assignment8():
    firstname = 'Shaked'
    lastname = 'Haimi'
    university = "Ben Gurion University"
    return render_template('assignment8.html',
                           profile={'name': firstname, 'lastName': lastname},
                           university=university,
                           hobbies=('Cooking', 'Reading', 'TV & Movies'),
                           favoritemovies=['Spirited Away', 'Inception'])


# ----Assignment 9-----#
users = {'user1': {'name': 'Shaked', 'email': 'shaked@gmail.com'},
         'user2': {'name': 'Ben', 'email': 'ben@gmail.com'},
         'user3': {'name': 'Amit', 'email': 'amit@gmail.com'},
         'user4': {'name': 'Shir', 'email': 'shir@gmail.com'},
         'user5': {'name': 'May', 'email': 'may@gmail.com'}}


def inputcheck(info):
    for user in users.values():
        if user['email'] == info or user['name'] == info:
            return user['email'], user['name']
    return False


@app.route('/assignment9', methods=['GET', 'POST'])
def assignment9():
    if request.method == 'GET':
        if 'searchInput' in request.args:
            print(request.args['searchInput'])
            if inputcheck(str(request.args['searchInput'])):
                email = inputcheck(request.args['searchInput'])[0]
                name = inputcheck(request.args['searchInput'])[1]
                return render_template('assignment9.html', name=name, email=email)
        return render_template('assignment9.html', users=users)
    if request.method == 'POST':
        nickname = request.form['nickName']
        session['username'] = nickname
        return render_template("assignment9.html", nickname=nickname, users=users)
    return render_template('assignment9.html', users=users)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session['username'] = ''
    return redirect(url_for('assignment9'))


# -------Assignment 11--------#

@app.route('/assignment11/users')
def assignment11_users():
    users_dictionary = {}
    query = "select * from users"
    result = interact_db(query, query_type='fetch')
    for user in result:
        users_dictionary[f'user_{user.id}'] = {
            'name': user.name,
            'email': user.email,
        }
    return jsonify(users_dictionary)


def get_user(id_num):
    user = requests.get(f' https://reqres.in/api/users/{id_num}')
    user = user.json()
    return user


@app.route('/assignment11/outer_source', methods=['GET', 'POST'])
def assignment11_outersource():
    if request.method == 'POST':
        id_num = request.form['id']
        user = get_user(id_num)
        return render_template('assignment11_outersource.html', user=user)
    return render_template('assignment11_outersource.html')


if __name__ == '__main__':
    app.run(debug=True)

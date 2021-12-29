from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello! How Can We Help?"


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


if __name__ == '__main__':
    app.run(debug=True)

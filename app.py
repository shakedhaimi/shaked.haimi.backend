import flask as f

app = f.Flask(__name__)


@app.route('/')
def home():
    return "Hello! How Can We Help?"


@app.route('/ContactUs')
def contact():
    return f.redirect(url_for('ContactForm')


@app.route('/CV')
def cv():
    return f.redirect('CV.html')


if __name__ == '__main__':
    app.run(debug=True)

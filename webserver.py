from flask import *
import time
ids = ["ATGDUZ5C7DS86CD8SVJ","HIUHYUITYR4456C47690"]
app = Flask(__name__)

@app.route('/error')
def error():
    return "<h1>You are not allowed to access this page >:(</h1>"

@app.route('/')
def index():
    return """<h1>Welcome to the home page</h1>
    <p>This is the home page of the website</p>
    <p>You can access the <a href="/controll">controll page </a></p>"""

@app.route('/controll/<name>')
def controll(name):
    if name in ids:
        return f"ID: {name} Authorised!"
        time.sleep(0.9)

    else:
        time.sleep(0.9)
        return redirect(url_for('error'))

if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<p>Home</p>"

@app.route("/about")
def about():
    return "<p>About</p>"

if __name__ == '__main__':
    app.run ()
    
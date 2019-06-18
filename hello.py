from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)  # construct an instance of Flask class for our webapp
app.debug = True  # Enable reloader and debugger

bootstrap = Bootstrap(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/user/<name>")
def user(name):
    return render_template("user.html", name=name)


if __name__ == "__main__":  # script executed directly?
    app.run()  # launch built-in web server and run this Flask webapp

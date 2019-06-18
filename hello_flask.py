"""
hell_flask: First Python-Flask webapp
"""
from flask import Flask, request, render_template

app = Flask(__name__)  # construct an instance of Flask class for our webapp
app.debug = True  # Enable reloader and debugger


@app.route("/")  # URL '/' to be handled by mian() route
def index():
    user_agent = request.headers.get("User-Agent")
    return "<p>Your browser is {}</p>".format(user_agent)


def main():
    return "Hello from flask."


@app.route("/hello")  # URL '/hello' to be handled by
def hello():
    return "Hello, World!"


@app.route("/hello/<username>")  # URL '/hello' to be handled by
def hello_username(username):
    return "Hello, {}".format(username)


@app.route("/hello/<int:userid>")  # URL '/hello' to be handled by
def hello_userid(userid):
    return "Hello, your ID is {:d}".format(userid)


if __name__ == "__main__":  # script executed directly?
    app.run()  # launch built-in web server and run this Flask webapp

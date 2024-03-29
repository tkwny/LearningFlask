from flask import Flask, render_template,session,redirect,url_for,flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment 
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)  # construct an instance of Flask class for our webapp
app.config['SECRET_KEY'] = 'kLmtT7MVNTXcmwvRUFQ6Myu2'
app.debug = True  # Enable reloader and debugger

moment = Moment(app)
bootstrap = Bootstrap(app)

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route("/", methods=['GET','POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session["name"] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html',form=form,name=session.get('name'))
    

@app.route("/user/<name>")
def user(name):
    return render_template("user.html", name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(e):
    render_template("500.html"), 500


if __name__ == "__main__":  # script executed directly?
    app.run()  # launch built-in web server and run this Flask webapp

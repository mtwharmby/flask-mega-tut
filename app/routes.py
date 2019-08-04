from flask import render_template
from app import app
from app.forms import LoginForm

# routes are the different URLs that the application implements.
# In Flask, handlers for the application routes are written as Python
# functions, called view functions.


@app.route('/')
@app.route('/index')
def index():
    """ A view function, which response to the / and /index urls"""
    # user & posts are faked input for the template
    # posts in the real thing will maintain the author and body fields of the dictionaries
    user = {'username': 'Michael'}
    posts = [{
             'author': {'username': 'John'},
             'body': 'Beautiful day in Portland!'
             },
             {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
             }]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
    # form=form passes the LoginForm as variable form to jinja2

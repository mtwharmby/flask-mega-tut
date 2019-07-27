from app import app

# routes are the different URLs that the application implements.
# In Flask, handlers for the application routes are written as Python
# functions, called view functions.


@app.route('/')
@app.route('/index')
def index():
    """ A simple view function, which response to the / and /index urls"""
    return 'Hello world!'

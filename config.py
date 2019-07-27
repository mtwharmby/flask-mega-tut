import os

# Config object allows separation of concerns, viz. app config vs. app logic etc.
# This is suggested to be a highly extensible pattern


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    # SECRET_KEY is used by Flask and some of its extensions as a
    # cryptographic key. In production, the OS environmental should be set!
    # - Flask-WTF uses it to protect web forms against Cross-Site Request
    #   Forgery (CSRF)

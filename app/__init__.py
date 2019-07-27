from flask import Flask

app = Flask(__name__)
# Name of module
# Name provides an entrypoint for flask for finding resources (e.g. templates)
# app here is an instance of Flask, which is a member of the app package

# Bottom import is a workaround to circular imports - routes needs to import
# app. Having this import at the end avoids this.
from app import routes

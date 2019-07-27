from flask import Flask
from config import Config

app = Flask(__name__)
# Name of module
# Name provides an entrypoint for flask for finding resources (e.g. templates)
# app here is an instance of Flask, which is a member of the app package

# Tells Flask to apply config from the Config object
app.config.from_object(Config)

# Bottom import is a workaround to circular imports - routes needs to import
# app. Having this import at the end avoids this.
from app import routes

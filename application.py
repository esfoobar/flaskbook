from flask import Flask

def create_app():
    app = Flask(__name__)

    # Load config
    app.config.from_pyfile('settings.py')

    return app
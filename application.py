from flask import Flask

def create_app():
    app = Flask(__name__)

    # Load config
    app.config.from_pyfile('settings.py')
    
    # import blueprints
    from user.views import user_app

    # register blueprints
    app.register_blueprint(user_app)

    return app
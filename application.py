from flask import Flask
from flask.ext.mongoengine import MongoEngine
from utilities.common import linkify, ms_stamp_humanize

db = MongoEngine()

def create_app(**config_overrides):
    app = Flask(__name__)

    # Load config
    app.config.from_pyfile('settings.py')
    
    # apply overrides for tests
    app.config.update(config_overrides)
    
    # setup db
    db.init_app(app)
    
    # import blueprints
    from user.views import user_app
    from relationship.views import relationship_app
    from feed.views import feed_app
    from home.views import home_app

    # register blueprints
    app.register_blueprint(user_app)
    app.register_blueprint(relationship_app)
    app.register_blueprint(feed_app)
    app.register_blueprint(home_app)
    
    app.context_processor(utility_processor)
    
    return app
    
def utility_processor():
  return dict(linkify=linkify, humanize=ms_stamp_humanize)
from flask import Flask
from roman_discovery import discover
from roman_discovery.flask import get_flask_rules


def create_app(config='newssite.config.DevConfig') -> Flask:
    flask_app = Flask(__name__)
    flask_app.config.from_object(config)

    rules = get_flask_rules("newssite", flask_app)
    discover("newssite", rules)
    return flask_app

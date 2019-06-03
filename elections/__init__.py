import os
import jinja2
from datetime import datetime

from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Register blueprints
    from elections import upcoming
    app.register_blueprint(upcoming.bp)

    # Register the template filter with the Jinja Environment
    app.jinja_env.filters['formatdatetime'] = format_datetime

    return app


# Jinja template filter to format a date nicely on the results page
def format_datetime(value, format="%b %d, %Y"):
    """Format a date time to (Default): d Mon YYYY HH:MM P"""
    if value is None:
        return ""
    else: 
        date = datetime.strptime(value, '%Y-%m-%dT%H:%M:%SZ')
        return date.strftime(format)
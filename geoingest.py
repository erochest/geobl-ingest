#!/usr/bin/env python3


"""The webapp to upload and ingest GeoTIFFs into Virgo."""


import os

from flask import Flask, request, session, g, redirect, url_for, abort, \
        render_template, flash
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import flask_migrate
from flask_assets import Environment, Bundle


CWD = os.path.dirname(__file__)


assets = Environment()
scss = Bundle('main.scss', filters='scss', output='css/style.css')
assets.register('css_all', scss)

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///geoingest.db'

    assets.init_app(app)
    app.config['ASSETS_LOAD_PATH'] = [
        os.path.join(CWD, 'sass'),
    ]
    #  assets.url = app.static_url_path
    #  assets.directory = app.static_folder
    #  assets.append_path('assets')

    db.init_app(app)
    migrate.init_app(app, db)

    @app.route('/')
    def upload_form():
        return render_template('index.html')

    return app


def init_db():
    """Initialize the database."""
    flask_migrate.migrate()


if __name__ == '__main__':
    manager = Manager(create_app())
    manager.add_command('db', MigrateCommand)

    manager.run()

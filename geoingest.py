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

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///geoingest.db'

assets = Environment(app)
assets.load_path = [
    os.path.join(CWD, 'sass'),
]

assets.url = app.static_url_path
assets.directory = app.static_folder
assets.append_path('assets')

scss = Bundle('main.scss', filters='scss', output='css/style.css')
assets.register('css_all', scss)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


def init_db():
    """Initialize the database."""
    flask_migrate.migrate()


@app.route('/')
def upload_form():
    return render_template('index.html')


if __name__ == '__main__':
    manager.run()

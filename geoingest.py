#!/usr/bin/env python3


"""The webapp to upload and ingest GeoTIFFs into Virgo."""


from flask import Flask, request, session, g, redirect, url_for, abort, \
        render_template, flash
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import flask_migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///geoingest.db'

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

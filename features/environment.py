"""Set up the environment for tests."""


from contextlib import closing
import os
import sqlite3
import sys
import tempfile

import geoingest


#  def before_step(context, step):
#  def after_step(context, step):
#  def before_scenario(context, scenario):
#  def after_scenario(context, scenario):
#  def before_tag(context, tag):
#  def after_tag(context, tag):


def before_feature(context, feature):
    context.client = context.app.test_client()


def after_feature(context, feature):
    """Clean out the database after each feature runs."""
    with closing(sqlite3.connect(context.app.config['DATABASE'])) as cxn:
        with closing(cxn.cursor()) as cursor:
            tables = list(cursor.execute('''
                SELECT name FROM sqlite_master WHERE type='table';
                '''))
            for (name,) in tables:
                cursor.execute('DELETE FROM {};'.format(name))


def before_all(context):
    """Set up the database before testing."""
    context.app = geoingest.create_app()
    context.db_fd, db_file = tempfile.mkstemp()
    context.app.config['DATABASE'] = db_file
    context.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_file
    context.app.config['TESTING'] = True
    with context.app.app_context():
        sys.stderr.write('\n*** initializing database: {} ({})\n\n'.format(
            context.app.config['SQLALCHEMY_DATABASE_URI'],
            os.path.exists(db_file),
        ))
        geoingest.init_db()


def after_all(context):
    """Delete the database after testing."""
    os.close(context.db_fd)
    os.unlink(context.app.config['DATABASE'])

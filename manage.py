# Flask-Migrate for the database changes.

from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
import os

from app import app, db

# Get the apps configs
app.config.from_object(os.environ['APP_SETTINGS'])
# Migrate the database
migrate = Migrate(app, db)
# manager for the migration.
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()

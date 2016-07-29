from flask_script import Manager, Shell
from app import app
from app import db
from app import models
from flask_migrate import Migrate, MigrateCommand


def make_shell_context():
    return dict(app=app, db=db, User=models.User, Role=models.Post)


manager = Manager(app)
manager.add_command("shell", Shell(make_context=make_shell_context))
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()

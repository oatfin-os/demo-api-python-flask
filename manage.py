from flask_script import Manager, Server

from apis.app import create_app
from apis.settings import app_config

app = create_app(app_config)

manager = Manager(app)
manager.add_command("runserver", Server(host="0.0.0.0"))

if __name__ == "__main__":
    manager.run()

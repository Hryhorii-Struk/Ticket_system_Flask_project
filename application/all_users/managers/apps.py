from flask import Flask

app = Flask(__name__)


class ManagersConfig:
    default_auto_field = 'BigTicketField'
    name = 'apps.all_users.managers'


if __name__ == '__main__':
    app.run()

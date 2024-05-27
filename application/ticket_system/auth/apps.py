from flask import Flask


class AuthConfig:
    name = 'apps.all_users.auth'
    label = '_auth'

    def __init__(self, app: Flask):
        self.app = app

    def init_app(self):
        pass


def all_users():
    return None
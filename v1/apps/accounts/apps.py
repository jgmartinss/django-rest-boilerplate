from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'v1.apps.accounts'

    def ready(self):
        from . import signals

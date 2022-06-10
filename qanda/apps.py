from django.apps import AppConfig


class QandaConfig(AppConfig):
    name = 'qanda'

    def ready(self):
        import qanda.signals
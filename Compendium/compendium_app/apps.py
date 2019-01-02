from django.apps import AppConfig


class CompendiumAppConfig(AppConfig):
    name = 'compendium_app'

    def ready(self):
        import compendium_app.signals



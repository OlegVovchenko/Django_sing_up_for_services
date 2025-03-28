from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
    verbose_name = 'Барбершоп'

    def ready(self):
        import core.signals  # Импорт сигналов из core.signals

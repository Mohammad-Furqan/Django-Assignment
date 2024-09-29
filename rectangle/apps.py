from django.apps import AppConfig


class RectangleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'rectangle'

    def ready(self):
        import rectangle.signals
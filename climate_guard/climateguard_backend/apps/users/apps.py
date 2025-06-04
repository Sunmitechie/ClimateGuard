from django.apps import AppConfig

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'climateguard_backend.apps.users'
    verbose_name = 'Users'

    def ready(self):
        try:
            import climateguard_backend.apps.users.signals  # noqa
        except ImportError:
            pass 
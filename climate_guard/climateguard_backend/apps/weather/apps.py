from django.apps import AppConfig
 
class WeatherConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'climateguard_backend.apps.weather'
    verbose_name = 'Weather' 
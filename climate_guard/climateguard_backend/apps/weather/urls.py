from django.urls import path
from . import views

app_name = 'weather'

urlpatterns = [
    path('forecast/', views.WeatherForecastView.as_view(), name='forecast'),
    path('current/', views.CurrentWeatherView.as_view(), name='current'),
    path('alerts/', views.WeatherAlertView.as_view(), name='alerts'),
    path('locations/', views.LocationView.as_view(), name='locations'),
    path('historical/', views.HistoricalWeatherView.as_view(), name='historical'),
] 
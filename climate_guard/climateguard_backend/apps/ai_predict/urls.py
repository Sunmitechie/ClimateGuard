from django.urls import path
from . import views

app_name = 'ai_predict'

urlpatterns = [
    path('risk-assessment/', views.RiskAssessmentView.as_view(), name='risk-assessment'),
    path('extreme-events/', views.ExtremeEventPredictionView.as_view(), name='extreme-events'),
    path('trends/', views.WeatherTrendView.as_view(), name='trends'),
    path('recommendations/', views.SafetyRecommendationView.as_view(), name='recommendations'),
] 
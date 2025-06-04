from django.urls import path
from . import views

app_name = 'ai_assist'
 
urlpatterns = [
    path('chat/', views.ChatView.as_view(), name='chat'),
    path('safety-tips/', views.SafetyTipsView.as_view(), name='safety-tips'),
    path('emergency-response/', views.EmergencyResponseView.as_view(), name='emergency-response'),
] 
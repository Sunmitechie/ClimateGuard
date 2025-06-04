from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('overview/', views.DashboardOverviewView.as_view(), name='overview'),
    path('analytics/', views.AnalyticsView.as_view(), name='analytics'),
    path('reports/', views.ReportsView.as_view(), name='reports'),
    path('settings/', views.DashboardSettingsView.as_view(), name='settings'),
] 
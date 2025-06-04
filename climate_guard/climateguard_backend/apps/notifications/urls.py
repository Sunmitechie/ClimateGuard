from django.urls import path
from . import views

app_name = 'notifications'

urlpatterns = [
    path('', views.NotificationListView.as_view(), name='list'),
    path('settings/', views.NotificationSettingsView.as_view(), name='settings'),
    path('mark-read/<int:pk>/', views.MarkNotificationReadView.as_view(), name='mark-read'),
    path('mark-all-read/', views.MarkAllNotificationsReadView.as_view(), name='mark-all-read'),
    path('subscribe/', views.NotificationSubscriptionView.as_view(), name='subscribe'),
] 
# tracking/urls.py

from django.urls import path
from .views import save_location, send_alert
from .views import track
urlpatterns = [
    path('save-location/', save_location, name='save_location'),
    path('send-alert/', send_alert, name='send_alert'),  # Add this line for the alert
    path('track/', track, name='track'),  
]


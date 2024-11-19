"""
URL configuration for woman project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from safety_app import views
# from .views import track
# from .views import save_location, send_alert

# from tracking import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('register/', views.register, name='register'),
    path('alert/', views.alert, name='alert'),
    path('success/', views.success, name='success'),
    path('about/', views.about, name='about'),
    path('track/', views.track, name='track'),
    path('map/', views.show_map, name='show_map'),
   # path('save-location/', save_location, name='save_location'),
   # path('send-alert/', send_alert, name='send_alert'), 
    # path('front/', views.front, name='front'),

]


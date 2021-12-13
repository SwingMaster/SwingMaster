from django.urls import path
from . import views

app_name = 'camera'

urlpatterns = [
    path('', views.home, name='home'),
    path('startCamera', views.base, name='base'),
    path('startCamera/recordVideo', views.detect, name='detect'),
    path('releaseCamera', views.releaseCamera, name='release'),
    path('backPage', views.backPage, name='backPage'),
]
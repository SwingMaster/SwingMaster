from django.urls import path
from . import views

app_name = 'camera'

urlpatterns = [
    path('', views.index, name='index'),
    path('camera', views.index2, name='index2'),
    path('camera/camera', views.detect, name="detect"),
]
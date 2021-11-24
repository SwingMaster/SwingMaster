from django.urls import path
from . import views

app_name = 'camera'

urlpatterns = [
    path('', views.index, name='index'),
    path('camera', views.detect, name="detect"),
]
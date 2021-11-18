from django.urls import path
from . import views

app_name = 'EditProfile'

urlpatterns = [
    path('', views.index, name='EditProfile'),
]
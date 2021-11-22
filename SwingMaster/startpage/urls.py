from django.urls import path
from . import views

app_name = 'startpage'

urlpatterns = [
    path('', views.index, name='startpage'),
]
from django.urls import path
from . import views

app_name = 'mainpage'

urlpatterns = [
    path('', views.index, name='mainpage'),
    path('logout/', views.logout, name='logout'),
]
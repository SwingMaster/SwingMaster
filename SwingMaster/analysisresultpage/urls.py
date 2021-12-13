from django.urls import path
from . import views

app_name = 'analysisresultpage'

urlpatterns = [
    path('', views.index, name='result'),
    path('saveScore/', views.saveScore, name="saveScore"),
]
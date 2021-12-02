from django.urls import path
from . import views

app_name = 'analysispage'

urlpatterns = [
    path('', views.index, name='index'),
    path('file_upload', views.file_upload, name="file_upload"),
]
from django.urls import path
from . import views

app_name = 'signup'

urlpatterns = [
    path('', views.index, name='signup'),
    path('checkDuplicatedId/', views.checkDuplicatedId, name='checkDuplicatedId'),
    path('checkDuplicatedNickname/', views.checkDuplicatedNickname, name='checkDuplicatedNickname'),
]
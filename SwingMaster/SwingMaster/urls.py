from django.contrib import admin
from django.urls import path, include

from startpage import views as views

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('mypage/', include('mypage.urls')),
    path('mainpage/', include('mainpage.urls')),
    path('signup/', include('signup.urls')),
    path('startpage/', include('startpage.urls')),
    path('EditProfile/', include('EditProfile.urls')),
    path('camera/', include('analysispage.urls')),
    path('result/', include('analysisresultpage.urls')),
]

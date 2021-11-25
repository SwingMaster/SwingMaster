<<<<<<< HEAD
"""SwingMaster URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
<<<<<<< HEAD
from startpage import views as views

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('mypage/', include('mypage.urls')),
    path('mainpage/', include('mainpage.urls')),
    path('signup/', include('signup.urls')),
    path('startpage/', include('startpage.urls')),
    path('EditProfile/', include('EditProfile.urls')),
=======

urlpatterns = [
    path('admin/', admin.site.urls),
    path('camera/', include('analysispage.urls')),
>>>>>>> origin/cjh_analysispage
]
=======
from django.conf.urls import include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('result/', include('analysisresultpage.urls')),
]

>>>>>>> origin/cjh_analysisresultpage

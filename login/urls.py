"""login URL Configuration

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
from django.urls import path
from django.conf.urls import url
from login_one import views
from django.contrib.auth.views import LoginView


urlpatterns = [

    url(r'^register/', views.register, name='register'),
    url(r'^$', LoginView.as_view(template_name='login/login1.html'), name='login_url'),
    url(r'^deshboard/', views.deshboardviews, name='deshboardviews'),
    url(r'^game/', views.game1, name='game'),

    path('admin/', admin.site.urls),
]
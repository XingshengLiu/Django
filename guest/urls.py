"""guest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, re_path
from sign import views

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'index/', views.index),  # 添加index/路径配置
    path(r'login_action/', views.login_action),  # 添加登录成功后的页面
    path(r'event_manage/', views.event_manage),
    re_path(r'^$', views.index),
    re_path(r'^index/$', views.index),
    re_path(r'^accounts/login/$', views.index),
]

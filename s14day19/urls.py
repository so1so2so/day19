"""s14day19 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from  app01 import views
from app03 import views as app03
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', views.index),
    url(r'^app03index/', app03.index),
    url(r'^app03login/', app03.login),
    url(r'^orm/', views.orm),
    url(r'^host/', views.host),
    url(r'^test_ajax$', views.test_ajax),
    # url(r'^login-(\d+).html', views.login),
    url(r'^detail-(\d+).html', views.detail),
]


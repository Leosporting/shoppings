"""shoppings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

from pcshoppings import  views



urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/', views.home),
    url(r'shoppings/', views.item_list_view,name='pc_shoppings_list1'),
    #url(r'shoppings/(?P<category>.*)$', views.pc_shoppings_list_view,name='pc_shoppings_list'),
    url(r'^$', views.pc_shoppings_list_view, name='home'),
    #url(r'pc_shoppings/(?P<category>.*)$', views.test_pc_shoppings),
    #url(r'^pc_shoppings/(?P<category>.*)$', views.pc_shoppings_list_view,  name = 'pc_shoppings_list'),
]

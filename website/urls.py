"""
URL configuration for mobapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from website.views import *

app_name= 'website'
urlpatterns = [
    path('', index_view, name='index'),
    path('features', features_view, name='features'),
    path('gallery', gallery_view, name='gallery'),
    path('pricing', pricing_view, name='pricing'),
    path('contact', contact_view, name='contact'),
    path('nothing_to_do', nothing_to_do_view, name='nothing_to_do'),
]
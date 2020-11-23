"""instaproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import include
from instaapp.views import logout_view

urlpatterns = [
    path('', include('instaapp.urls')),
    path('landing-page/', include('instaapp.urls')),
    path('profile/<id>/', include('instaapp.urls')),
    path('upload_pic/', include('instaapp.urls')),
    path('update-profile/', include('instaapp.urls')),
    path('search/', include('instaapp.urls')),
     path('image/<image_id>/', include('instaapp.urls')),

    path('accounts/', include('django_registration.backends.activation.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_view),
    path('admin/', admin.site.urls),
]
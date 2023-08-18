"""
URL configuration for web_django project.

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
# from django.contrib import admin
from django.urls import path
# from django.urls import re_path
from rest_framework_swagger.views import get_swagger_view

from app01.views.make_data import makedata
from app01.views import users,scripts,needs

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    # path("admin/", admin.site.urls),
    # re_path(r'^$', schema_view),
    # path(r'oauth/', include('oauth2_provider.urls', namespace='oauth2_provider')),

    # re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_URL}, name='static'),

    path("users/login", users.login),
    path("users/register", users.register),
    path("users/logout", users.logout),

    path("scripts", scripts.scripts_list),
    path("scripts/detail", scripts.scripts_detail),
    path("scripts/upload", scripts.upload),
    path("scripts/star", scripts.star),

    path("needs", needs.needs_list),
    path("needs/upload", needs.upload),

    path("makedata", makedata),


]

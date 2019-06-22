from django.contrib import admin
from django.shortcuts import render
from django.urls import include, path
from django.views import View

from fightme import api as api_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-rest/', include(api_urls.router.urls)),
    path('api/', include(api_urls)),
]

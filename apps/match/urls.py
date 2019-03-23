from django.urls import path, include

from rest_framework import routers

from .api.views import MatchViewSet


router = routers.DefaultRouter()
router.register(r'matches', MatchViewSet)

urlpatterns = [
    path('', include(router.urls))
]

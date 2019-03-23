from django.urls import path, include

from rest_framework import routers

from .api.views import PlayerViewSet, GameViewSet


router = routers.DefaultRouter()
router.register(r'games', GameViewSet)
router.register(r'players', PlayerViewSet)

urlpatterns = [
    path('', include(router.urls))
]

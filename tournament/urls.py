from django.urls import path, include

from rest_framework import routers

from .api.views import TournamentViewSet


router = routers.DefaultRouter()
router.register(r'tournaments', TournamentViewSet)

urlpatterns = [
    path('', include(router.urls))
]

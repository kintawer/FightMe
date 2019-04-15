from django.urls import path, include

from rest_framework import routers

from .api.views import RatingViewSet


router = routers.DefaultRouter()
router.register(r'ratings', RatingViewSet)

urlpatterns = [
    path('', include(router.urls))
]

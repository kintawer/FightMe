from django.urls import path, include

from rest_framework import routers

from .api.views import AccountViewSet


router = routers.DefaultRouter()
router.register(r'accounts', AccountViewSet)

urlpatterns = [
    path('', include(router.urls))
]

from rest_framework import viewsets

from .serializers import RatingSerializer
from ..models import Rating


class RatingViewSet(viewsets.ModelViewSet):
    """
    API ratings
    """
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

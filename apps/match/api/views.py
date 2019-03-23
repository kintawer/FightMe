from rest_framework import viewsets

from .serializers import MatchSerializer
from ..models import Match


class MatchViewSet(viewsets.ModelViewSet):
    """
    API matches
    """
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

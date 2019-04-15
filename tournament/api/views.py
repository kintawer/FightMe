from rest_framework import viewsets

from .serializers import TournamentSerializer
from ..models import Tournament


class TournamentViewSet(viewsets.ModelViewSet):
    """
    API tournaments
    """
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer

from rest_framework import viewsets

from .serializers import GameSerializer, PlayerSerializer
from ..models import Game, Player


class GameViewSet(viewsets.ModelViewSet):
    """
    API games
    """
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    """
    API players
    """
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

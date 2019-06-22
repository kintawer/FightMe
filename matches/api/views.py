from rest_framework import viewsets

from matches.api.serializers import (SimpleMatchSerializer,
                                     TournamentMatchSerializer)
from matches.models import SimpleMatch, TournamentMatch


class SimpleMatchViewSet(viewsets.ModelViewSet):

    queryset = SimpleMatch.objects.all()
    serializer_class = SimpleMatchSerializer


class TournamentMatchViewSet(viewsets.ModelViewSet):

    queryset = TournamentMatch.objects.all()
    serializer_class = TournamentMatchSerializer

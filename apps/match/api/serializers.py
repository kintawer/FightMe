from rest_framework import serializers

from ..models import Match


class MatchSerializer(serializers.HyperlinkedModelSerializer):

    # todo: внешние модели
    class Meta:
        model = Match
        fields = (
            'id',
            'url',
            'winner',
            'loser',
            'tournament',
            'status',
        )

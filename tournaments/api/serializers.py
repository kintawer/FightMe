from rest_framework import serializers

from ..models import Tournament


class TournamentSerializer(serializers.HyperlinkedModelSerializer):

    # todo: внешние модели
    class Meta:
        model = Tournament
        fields = (
            'id',
            'url',
            'name',
            'game',
        )

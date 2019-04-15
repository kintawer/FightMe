from rest_framework import serializers

from ..models import Game, Player


class GameSerializer(serializers.HyperlinkedModelSerializer):

    # todo: внешние модели
    class Meta:
        model = Game
        fields = (
            'id',
            'url',
            'name',
        )


class PlayerSerializer(serializers.HyperlinkedModelSerializer):

    # todo: внешние модели
    class Meta:
        model = Player
        fields = (
            'id',
            'url',
            'nickname',
        )

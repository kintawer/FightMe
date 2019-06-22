from rest_framework import serializers

from games.models import Game, Platform


class GameSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Game
        fields = ('id', 'url', 'name',)

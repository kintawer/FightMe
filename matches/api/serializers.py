from rest_framework import serializers

from matches.models import SimpleMatch, TournamentMatch


class SimpleMatchSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = SimpleMatch
        fields = (
            'id',
            'url',
            'winner',
            'loser',
            'tournament',
            'status',
        )


class TournamentMatchSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = TournamentMatch
        fields = (
            'id',
            'url',
            'winner',
            'loser',
            'tournament',
            'status',
        )

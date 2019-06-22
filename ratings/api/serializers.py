from rest_framework import serializers

from ..models import Rating


class RatingSerializer(serializers.HyperlinkedModelSerializer):

    # todo: внешние модели
    class Meta:
        model = Rating
        fields = (
            'id',
            'player',
            'rating',
        )

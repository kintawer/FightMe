from rest_framework import serializers

from accounts.models import Account


class AccountPublicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account
        fields = (
            'id',
            'url',
            'user',
            'game',
            'nickname',
        )

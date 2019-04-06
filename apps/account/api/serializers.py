from rest_framework import serializers

from ..models import Account


class AccountPrivateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = (
            'id',
            'username',
            'email',
            'is_active',
            'balance',
        )


class AccountPublicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account
        fields = (
            'id',
            'url',
            'username',
            'balance',
        )

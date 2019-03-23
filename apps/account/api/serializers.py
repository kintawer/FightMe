from rest_framework import serializers

from ..models import Account


class AccountSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Account
        fields = (
            'id',
            'url',
            'username',
            'first_name',
            'last_name',
            'email',
            'is_active',
            'balance',
        )

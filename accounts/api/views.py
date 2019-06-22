from rest_framework import permissions, viewsets, views
from rest_framework.response import Response

from .serializers import AccountPublicSerializer
from ..models import Account


class AccountViewSet(viewsets.ModelViewSet):
    """
    API public accounts
    """
    queryset = Account.objects.all()
    serializer_class = AccountPublicSerializer

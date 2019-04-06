from rest_framework import permissions, viewsets, views
from rest_framework.response import Response

from .serializers import AccountPublicSerializer, AccountPrivateSerializer
from ..models import Account


class AccountViewSet(viewsets.ModelViewSet):
    """
    API public accounts
    """
    queryset = Account.objects.all()
    serializer_class = AccountPublicSerializer


class AccountAPIView(views.APIView):
    """
    API private account
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        account = Account.objects.get(pk=request.user.id)
        serializer = AccountPrivateSerializer(account)
        return Response(data={'data': serializer.data}, status=200)

from rest_framework import viewsets, generics
from rest_framework.response import Response
from knox.models import AuthToken

from users.models import User
from users.api.serializers import UserSerializer, CreateUserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CreateUserAPIView(generics.CreateAPIView):
    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs):
        user_serializer = self.get_serializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()

        token, _ = AuthToken.objects.create(user=user)
        return Response({
            "user": user_serializer.validated_data,
            "token": token.digest,
        })

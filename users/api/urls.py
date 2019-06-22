from django.urls import path
from users.api.views import CreateUserAPIView


urlpatterns = [
    path('register/', CreateUserAPIView.as_view(), name='register'),

]
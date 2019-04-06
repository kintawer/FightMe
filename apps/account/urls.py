from django.urls import path, include
from .views import Logout


urlpatterns = [
    path('', include('social_django.urls', namespace='social')),
    path('logout/', Logout.as_view()),
]



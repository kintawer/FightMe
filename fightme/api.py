from django.urls import path, include

from rest_framework import routers

from accounts.api.views import AccountViewSet
from games.api.views import GameViewSet
from matches.api.views import SimpleMatchViewSet, TournamentMatchViewSet
from ratings.api.views import RatingViewSet
from tournaments.api.views import TournamentViewSet
from users.api.views import UserViewSet

# API urls
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'accounts', AccountViewSet)
router.register(r'games', GameViewSet)
router.register(r'simple-matches', SimpleMatchViewSet)
router.register(r'tournament-matches', TournamentMatchViewSet)
router.register(r'ratings', RatingViewSet)
router.register(r'tournaments', TournamentViewSet)

urlpatterns = [
    path('users/', include('users.api.urls')),
    path('accounts/', include('accounts.api.urls')),
    path('games/', include('games.api.urls')),
    path('matches/', include('matches.api.urls')),
    path('tournaments/', include('tournaments.api.urls')),
    path('ratings/', include('ratings.api.urls')),
]

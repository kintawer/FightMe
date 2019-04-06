from django.contrib import admin
from django.shortcuts import render
from django.views import View
from django.urls import path, include

from rest_framework import routers

from apps.account.api.views import AccountViewSet, AccountAPIView
from apps.game.api.views import GameViewSet, PlayerViewSet
from apps.match.api.views import MatchViewSet
from apps.rating.api.views import RatingViewSet
from apps.tournament.api.views import TournamentViewSet


# API urls
router = routers.DefaultRouter()
router.register(r'accounts', AccountViewSet)
router.register(r'games', GameViewSet)
router.register(r'players', PlayerViewSet)
router.register(r'matches', MatchViewSet)
router.register(r'ratings', RatingViewSet)
router.register(r'tournaments', TournamentViewSet)

class Test(View):
    def get(self, request):
        return render(request, 'index.html')

urlpatterns = [
    path('', Test.as_view()),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/account/', AccountAPIView.as_view()),
    path('account/', include('apps.account.urls'))

]

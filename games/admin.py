from django.contrib import admin

from games.models import Game, Platform


admin.site.register(Game)
admin.site.register(Platform)

from django.contrib import admin

from matches.models import SimpleMatch, TournamentMatch


admin.site.register(SimpleMatch)
admin.site.register(TournamentMatch)

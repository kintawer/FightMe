from django.db import models

from game import Game, Player


class Tournament(models.Model):
    name = models.CharField('Название', max_length=255, blank=False, null=False)
    game = models.ForeignKey(Game, on_delete=models.DO_NOTHING)
    players = models.ManyToManyField(Player)

    class Meta:
        db_table = 'core_tournament'

from django.db import models
from apps.account.models import Account


class Game(models.Model):
    name = models.CharField('Название', max_length=255, blank=False, null=False)
    players = models.ManyToManyField(Account, through='Player', verbose_name='Игроки')

    class Meta:
        db_table = 'core_game'


class Player(models.Model):
    player = models.ForeignKey(Account, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=True)
    nickname = models.CharField('Никнейм', max_length=50, blank=False, null=False)

from django.db import models

from game import Game, Player
from tournament import Tournament


MATCH_STATUSES = (
    (0, 'Ожидание'),
    (1, 'Завершен'),
    (2, 'Отменен'),
)


class Match(models.Model):
    game = models.ForeignKey(Game, on_delete=models.DO_NOTHING, verbose_name='Игра')
    winner = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='winner', verbose_name='Победитель')
    loser = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='loser', verbose_name='Проигравший')
    tournament = models.ForeignKey(Tournament, default=None, null=True, on_delete=models.CASCADE, verbose_name='Турнир')
    status = models.SmallIntegerField('Статус', default=0, blank=False, null=False, choices=MATCH_STATUSES)

    class Meta:
        db_table = 'core_match'

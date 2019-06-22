from django.db import models


MATCH_STATUSES = (
    (-1, 'Отменен'),
    (0, 'Ожидание'),
    (1, 'Завершен'),
    (2, 'Окончен в ничью'),
)


class SimpleMatch(models.Model):
    game = models.ForeignKey(verbose_name='Игра',
                             to='games.Game',
                             on_delete=models.DO_NOTHING,
                             related_name='simple_matches')
    winner = models.ForeignKey(verbose_name='Победитель',
                               to='accounts.Account',
                               on_delete=models.CASCADE,
                               related_name='win_matches')
    loser = models.ForeignKey(verbose_name='Проигравший',
                              to='accounts.Account',
                              on_delete=models.CASCADE,
                              related_name='los_matches')
    status = models.SmallIntegerField(verbose_name='Статус',
                                      choices=MATCH_STATUSES,
                                      default=0,
                                      blank=False,
                                      null=False)
    complete_time = models.DateTimeField(verbose_name='Время окончания',
                                         blank=True,
                                         null=True)

    class Meta:
        unique_together = ['winner', 'loser']

        verbose_name = 'Обычный матч'
        verbose_name_plural = 'Обычные матчи'


class TournamentMatch(models.Model):
    winner = models.ForeignKey(verbose_name='Победитель',
                               to='accounts.Account',
                               on_delete=models.CASCADE,
                               related_name='winner')
    loser = models.ForeignKey(verbose_name='Проигравший',
                              to='accounts.Account',
                              on_delete=models.CASCADE,
                              related_name='loser')
    tournament = models.ForeignKey(verbose_name='Турнир',
                                   to='tournaments.Tournament',
                                   default=None,
                                   null=True,
                                   on_delete=models.CASCADE)
    status = models.SmallIntegerField(verbose_name='Статус',
                                      default=0,
                                      blank=False,
                                      null=False,
                                      choices=MATCH_STATUSES)

    class Meta:
        unique_together = ['winner', 'loser']

        verbose_name = 'Турнирный матч'
        verbose_name_plural = 'Турнирные матчи'

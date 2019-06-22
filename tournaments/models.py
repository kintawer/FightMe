from django.db import models


class Tournament(models.Model):
    name = models.CharField(verbose_name='Название',
                            max_length=255,
                            blank=False,
                            null=False)
    game = models.ForeignKey(verbose_name='Игра',
                             to='games.Game',
                             on_delete=models.CASCADE)
    participants = models.ManyToManyField(to='accounts.Account',
                                          through='tournaments.Participant',
                                          related_name='tournaments')

    class Meta:
        verbose_name = 'Турнир'
        verbose_name_plural = 'Турниры'


class Participant(models.Model):
    account = models.ForeignKey(verbose_name='Аккаунт',
                                to='accounts.Account',
                                on_delete=models.CASCADE)
    tournament = models.ForeignKey(verbose_name='Турнир',
                                   to='tournaments.Tournament',
                                   on_delete=models.CASCADE)
    status = models.ManyToManyField(to='tournaments.ParticipantStatus',
                                    through='tournaments.ParticipantStatusHistory')

    class Meta:
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'


class ParticipantStatus(models.Model):
    name = models.CharField(verbose_name='Название',
                            max_length=50,
                            blank=False,
                            null=False)

    class Meta:
        verbose_name = 'Статус участника турнира'
        verbose_name_plural = 'Статусы участника турнира'


class ParticipantStatusHistory(models.Model):
    participant = models.ForeignKey(verbose_name='Участник', to='tournaments.Participant',
                                    on_delete=models.DO_NOTHING)
    status = models.ForeignKey(verbose_name='Статус',
                               to='tournaments.ParticipantStatus',
                               on_delete=models.CASCADE,
                               null=False)
    time = models.DateTimeField(verbose_name='Время',
                                auto_now=True)

    class Meta:
        verbose_name = 'История статуса'
        verbose_name_plural = 'История статусов'

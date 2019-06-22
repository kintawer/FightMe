from django.db import models


class Game(models.Model):
    name = models.CharField(verbose_name='Название',
                            max_length=255,
                            blank=False,
                            null=False)
    platform = models.ForeignKey(verbose_name='Платформа',
                                 to='games.Platform',
                                 on_delete=models.CASCADE)
    players = models.ManyToManyField(verbose_name='Игроки',
                                     to='users.User',
                                     through='accounts.Account',
                                     related_name='games')

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'


class Platform(models.Model):
    name = models.CharField(verbose_name='Название',
                            max_length=20,
                            blank=False,
                            null=False)

    class Meta:
        verbose_name = 'Платформа'
        verbose_name_plural = 'Платформы'

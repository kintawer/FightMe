from django.db import models


class Rating(models.Model):
    account = models.OneToOneField(verbose_name='Аккаунт',
                                   to='accounts.Account',
                                   on_delete=models.CASCADE)
    rating = models.IntegerField(verbose_name='Рейтинг',
                                 default=1000)

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'

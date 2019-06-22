from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils import timezone


class Account(models.Model):
    user = models.ForeignKey(verbose_name='Пользователь',
                             to='users.User',
                             on_delete=models.CASCADE,
                             related_name='accounts')
    game = models.ForeignKey(verbose_name='Игра',
                             to='games.Game',
                             on_delete=models.CASCADE,
                             related_name='accounts')
    nickname = models.CharField(verbose_name='Никнейм',
                                max_length=50,
                                blank=False,
                                null=False)

    class Meta:
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккаунты'

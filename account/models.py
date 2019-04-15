from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils import timezone


class Account(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()
    username = models.CharField('username', max_length=150, unique=True,
                                help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
                                error_messages={
                                    'unique': "A user with that username already exists.",
                                },
                                validators=[username_validator])
    email = models.EmailField('email address', blank=True)
    is_staff = models.BooleanField('staff status', default=False)
    is_active = models.BooleanField('active', default=True)
    date_joined = models.DateTimeField('date joined', default=timezone.now)

    balance = models.IntegerField('balance', default=0, blank=False, null=False)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = 'account'
        verbose_name_plural = 'accounts'
        db_table = 'core_account'

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_username(self):
        return self.username

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager


class User(AbstractUser):
    city = models.CharField(
        _('Город'),
        max_length=255,
        blank=True
    )
    job = models.CharField(
        _('Работа'),
        max_length=255,
        blank=True
    )
    status = models.TextField(
        _('Статус'),
        blank=True
    )

    objects = UserManager()

    def get_full_name(self):
        full_name = super().get_full_name()
        return f'{full_name} ({self.username})' if full_name else self.username

    class Meta(AbstractUser.Meta):
        ordering = ('username',)

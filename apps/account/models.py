from django.db import models

from django.contrib.auth.models import AbstractUser

from django.utils.translation import  ugettext_lazy as _


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

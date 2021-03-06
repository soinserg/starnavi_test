from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class AccountConfig(AppConfig):
    name = 'apps.account'
    verbose_name = _('Аккаунты')

    def ready(self):
        from . import signals

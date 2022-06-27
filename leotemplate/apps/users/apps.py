from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "leotemplate.apps.users"
    verbose_name = _('유저')

    def ready(self):
        try:
            import leotemplate.apps.users.signals  # noqa F401
        except ImportError:
            pass

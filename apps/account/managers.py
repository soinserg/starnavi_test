from django.contrib.auth.models import UserManager as BaseUserManager


class UserManager(BaseUserManager):
    def visitors(self):
        return self.filter(is_staff=False)

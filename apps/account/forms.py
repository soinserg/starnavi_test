from django.contrib.auth.forms import UserCreationForm

from .models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2',
                  'first_name', 'last_name', 'email',
                  'city', 'job', 'status']

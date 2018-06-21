from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView, DetailView

from .forms import SignUpForm
from .models import User


class SignUp(FormView):
    form_class = SignUpForm
    success_url = reverse_lazy('core:base')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super(SignUp, self).form_valid(form)


class UserList(ListView):
    queryset = User.objects.visitors()


class UserDetail(DetailView):
    queryset = User.objects.visitors()

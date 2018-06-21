from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import SignUpForm


class SignUp(FormView):
    form_class = SignUpForm
    success_url = reverse_lazy('core:base')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super(SignUp, self).form_valid(form)

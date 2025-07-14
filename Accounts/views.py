from django.views.generic import TemplateView
#Login Module
from django.contrib.auth.views import LoginView as authLoginView
#LoginRequired
from django.contrib.auth.mixins import LoginRequiredMixin
#Logout 
from django.contrib.auth.views import LogoutView as authLogoutView

from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
# Create your views here.

class RegisterView(FormView):
    template_name = 'accounts/register.html'
    form_class = UserCreationForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    success_url = reverse_lazy("login")

class LoginView(authLoginView):
    template_name = 'auth/login.html'
    redirect_authenticated_user =True # redirect to Dashboard 

class LogoutView(authLogoutView):
    next_page = 'login'

# from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
class DashboardView(LoginRequiredMixin,TemplateView):
    template_name = 'accounts/dashboard.html'
    # login_url = "login"


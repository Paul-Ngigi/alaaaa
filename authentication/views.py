from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.views.generic import View
from .forms import LoginForm
from django.contrib import messages

User = get_user_model()


# Create your views here.
class SignUp(View):
    """
    Sign up view
    """

    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass


class Login(View):
    """
    Sign in view
    """
    template_name = 'authentication/signin.html'
    form = LoginForm

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home_view')

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(request, username=username, password=password)

            if user is None:
                messages.error(request, "Invalid Login", extra_tags="error")
                return render(request, self.template_name)

            login(request, user)
            messages.success(request, f"Welcome {user.username}", extra_tags="success")
            return redirect('home_view')


class SignOut(View):
    """
    Sign out view
    """

    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect('login_view')

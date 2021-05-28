from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.views.generic import View
from .forms import LoginForm, SignOutForm
from django.contrib import messages

User = get_user_model()


# Create your views here.
class SignUp(View):
    """
    Sign up view
    """
    title = 'signup'

    form = SignOutForm
    template_name = 'authentication/signup.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home_view')

    def post(self, request, *args, **kwargs):
        form = self.form(request.post or None)
        if form.is_valid():
            username = form.cleaned_data("username")
            email = form.cleaned_data("email")
            password = form.cleaned_data("password1")
            password2 = form.cleaned_data("password2")

            user = User.objects.create_user(username, email, password)

            return redirect('signin_view')

        context = {"title": self.title, "user": self.user}

        return render(request, self.template_name, context)


class Login(View):
    """
    Sign in view
    """
    title = 'Login'

    form = LoginForm
    template_name = 'authentication/signin.html'
    context = {"title", title}

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
                return render(request, self.template_name, self.context)

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

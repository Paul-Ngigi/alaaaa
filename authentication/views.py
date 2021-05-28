from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.views.generic import View
from .forms import RegistrationForm
from django.contrib import messages

User = get_user_model()


# Create your views here.
class SignUp(View):
    """
    Sign up view
    """
    title = 'signup'

    form = RegistrationForm
    template_name = 'authentication/signup.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home_view')

    def post(self, request, *args, **kwargs):
        form = self.form()
        if request.method == 'POST':
            form = form(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login_view')

        else:
            form = form()

        context = {"form": form, "title": self.title}
        return render(request, self.template_name, context)


class Login(View):
    """
    Login view
    """
    title = 'Login'

    template_name = 'authentication/signin.html'
    context = {"title", title}

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home_view')
        else:
            return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        context = self.context

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            if username and password:

                user = authenticate(request, username=username, password=password)

                if user is not None:
                    login(request, user)
                    messages.success(request, f"Welcome to Awards", extra_tags="success")
                    return redirect('home_view')

                else:
                    messages.error(request, "Invalid Login", extra_tags="error")
                    return render(request, self.template_name)

        return render(request, self.template_name)


class SignOut(View):
    """
    Sign out view
    """

    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect('login_view')

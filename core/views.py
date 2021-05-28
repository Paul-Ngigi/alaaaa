from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

User = get_user_model()


# Create your views here.
class IndexView(View):
    user = User

    @login_required
    def get(self, request, *args, **kwargs):
        template_name = 'core/index.html'
        title = 'Home'
        context = {"title": title}

        return render(request, template_name, context)

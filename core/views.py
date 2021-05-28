from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your views here.
class IndexView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'core/index.html'
        title = 'Home'
        context = {"title": title}

        return render(request, template_name, context)

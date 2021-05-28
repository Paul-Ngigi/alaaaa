from django.urls import path
from .views import IndexView

# Core Urls
urlpatterns = [
    path('', IndexView.as_view(), name='index_view')  # Url to the home page,
]

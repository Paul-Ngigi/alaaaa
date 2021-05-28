from django.urls import path
from .views import SignUp, Login, SignOut
from core.views import IndexView

# Authentication urls
urlpatterns = [
    path('', Login.as_view(), name='login_view'),
    path('home/', IndexView.as_view(), name='home_view'),
    path('signup/', SignUp.as_view(), name='signup_view'),
    path('signout/', SignOut.as_view(), name='signout_view')
]

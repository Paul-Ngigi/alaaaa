from django.urls import path
from .views import SignUp, Login, SignOut

# Authentication urls
urlpatterns = [
    path('', Login.as_view(), name='login_view'),
    path('signup/', SignUp.as_view(), name='signup_view'),
    path('signout/', SignOut.as_view(), name='signout_view')
]

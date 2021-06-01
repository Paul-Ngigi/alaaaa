from django.urls import path
from .views import IndexView, PostsDetails, voting

# Core Urls
urlpatterns = [
    path('', IndexView.as_view(), name='index_view'), # Url to the home page,
    path('post/<int:pk>/', PostsDetails.as_view(), name='details_view'), # Url to the posts details page,
    path('vote/<int:pk>/', voting, name='votes_view'), # Url to the vote page,
]

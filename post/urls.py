from django.urls import path
from post.views import postformview, posts, loginuser

urlpatterns = [
    path("form/", postformview, name="form"),
    path("posts/", posts, name="posts"),
    path("loginuser/", loginuser, name="loginuser"),
]
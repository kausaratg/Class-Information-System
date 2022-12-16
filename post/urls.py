from django.urls import path
from post.views import postformview, posts, loginuser, postdetail, logout_user

urlpatterns = [
    path("form/", postformview, name="form"),
    path("posts/", posts, name="posts"),
    path("loginuser/", loginuser, name="loginuser"),
    path("postdetail/<int:pk>", postdetail, name="postdetail"),
    path("logout_user", logout_user, name="logout_user"),

]
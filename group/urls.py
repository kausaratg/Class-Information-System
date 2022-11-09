from django.urls import path
from group.views import class_group, index


urlpatterns = [
    path("",  index, name="index"),
    path("group/", class_group, name="class_group")
]
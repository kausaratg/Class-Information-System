from django.urls import path
from group.views import class_group


urlpatterns = [
    path("group/", class_group, name="class_group")
]
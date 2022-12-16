from django.urls import path
from timetable.views import timetable, timetable_c

urlpatterns = [
    path("timetable", timetable, name="timetable"),
    path("timetable_c", timetable_c, name="timetable_c"),
]

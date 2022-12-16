from django.urls import path
from timetable.views import timetable, timetable_c, timetable_a, timetable_d, timetable_b

urlpatterns = [
    path("timetable", timetable, name="timetable"),
    path("timetable_a", timetable_a, name="timetable_a"),
    path("timetable_d", timetable_d, name="timetable_d"),
    path("timetable_c", timetable_c, name="timetable_c"),
    path("timetable_b", timetable_b, name="timetable_b"),
]

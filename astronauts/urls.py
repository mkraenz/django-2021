from django.urls import path

from astronauts.views import get_astronauts

urlpatterns = [
    path("", get_astronauts, name="astronauts-list"),
]

from typing import List, TypedDict

import requests
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render


class Astronaut(TypedDict):
    name: str
    craft: str


class AstronautsApiRes(TypedDict):
    message: str
    number: int
    people: List[Astronaut]


def get_astronauts(request: HttpRequest) -> HttpResponse:
    url = "http://api.open-notify.org/astros.json"
    res = requests.get(url)
    data: AstronautsApiRes = res.json()
    return render(
        request,
        "astronauts/index.html",
        {"number_of_people": data["number"], "people": data["people"]},
    )

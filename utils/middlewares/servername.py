# https://stackoverflow.com/questions/47937566/how-to-calculate-response-time-in-django

import random
from typing import Callable

from django.http import HttpRequest, HttpResponse

name = f"server_{random.randint(0,9000)}"


def servername(
    get_response: Callable[[HttpRequest], HttpResponse]
) -> Callable[[HttpRequest], HttpResponse]:
    def middleware(request: HttpRequest):
        response: HttpResponse = get_response(request)

        response["X-Server-Name"] = name
        return response

    return middleware

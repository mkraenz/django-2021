# https://stackoverflow.com/questions/47937566/how-to-calculate-response-time-in-django

import time
from typing import Callable

from django.http import HttpRequest, HttpResponse


def stats_middleware(
    get_response: Callable[[HttpRequest], HttpResponse]
) -> Callable[[HttpRequest], HttpResponse]:
    def middleware(request: HttpRequest):
        start_time = time.time()

        response: HttpResponse = get_response(request)

        duration = time.time() - start_time

        response["X-Page-Generation-Duration-ms"] = int(duration * 1000)
        return response

    return middleware

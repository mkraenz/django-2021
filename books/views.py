
# Create your views here.
from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Books, Books, Bux.")

from django.http import HttpRequest, HttpResponse, HttpResponseRedirect


def language_redirect(request: HttpRequest, new_lang: str) -> HttpResponse:
    return HttpResponseRedirect(new_lang)

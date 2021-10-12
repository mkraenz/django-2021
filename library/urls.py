"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from books.rest import BookViewSet, ChapterViewSet
from library.views import language_redirect
from snippets.serializers import UserViewSet
from snippets.views import SnippetHighlight, SnippetViewSet

from .settings import ADMIN_URL

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register("books", BookViewSet)
router.register("chapters", ChapterViewSet)
router.register("snippets", SnippetViewSet)
router.register("users", UserViewSet)

localized_urlpatterns = i18n_patterns(
    path("", include("library.localizer.urls")),
    path("books/", include("books.urls")),
    path("astronauts/", include("astronauts.urls")),
    path("i18n/", include("django.conf.urls.i18n")),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    prefix_default_language=True,
)


urlpatterns = [
    path("rest/", include(router.urls)),
    path(
        "rest/snippets/<int:pk>/highlight/",
        SnippetHighlight.as_view(),
        name="snippet-highlight",
    ),
    path("<str:new_lang>", language_redirect, name="language-redirect"),
    path(ADMIN_URL, admin.site.urls),
    *localized_urlpatterns,
]

from django.urls import path

from snippets.serializers import UserViewSet
from snippets.views import SnippetHighlight

urlpatterns = [
    path("users/", UserViewSet.as_view({"get": "list"}), name="user-list"),
    path(
        "users/<int:pk>/", UserViewSet.as_view({"get": "retrieve"}), name="user-detail"
    ),
    path(
        "snippets/<int:pk>/highlight/",
        SnippetHighlight.as_view(),
        name="snippet-highlight",
    ),
]

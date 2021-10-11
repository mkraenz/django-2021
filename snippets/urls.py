from django.urls import path

from snippets.serializers import UserDetails, UserList
from snippets.views import SnippetHighlight, api_root2

urlpatterns = [
    path("users/", UserList.as_view(), name="users"),
    path("users/<int:pk>/", UserDetails.as_view(), name="user-detail"),
    path("bla/", api_root2, name="api-root2"),  # not working :/
    path(
        "snippets/<int:pk>/highlight/",
        SnippetHighlight.as_view(),
        name="snippet-highlight",
    ),
]

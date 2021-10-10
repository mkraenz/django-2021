from django.urls import path

from snippets.serializers import UserDetails, UserList

urlpatterns = [
    path("users/", UserList.as_view(), name="users"),
    path("users/<int:pk>", UserDetails.as_view(), name="user-detail"),
]

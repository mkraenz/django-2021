from rest_framework import permissions
from rest_framework.request import Request
from rest_framework.views import APIView

from snippets.models import Snippet


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: APIView, obj: Snippet):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user

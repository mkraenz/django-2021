from typing import Optional

from rest_framework import generics, permissions, renderers, serializers, viewsets
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.reverse import reverse

from snippets.models import Snippet
from snippets.permissions import IsOwnerOrReadOnly


class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:  # type: ignore
        model = Snippet
        fields = ["id", "title", "code", "linenos", "language", "style", "owner"]
        read_only_fields = ["owner"]


class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer: serializers.BaseSerializer) -> None:
        serializer.save(owner=self.request.user)


class SnippetHighlight(generics.GenericAPIView):
    queryset = Snippet.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request: Request, *args: str, **kwargs: str) -> Response:
        snippet: Snippet = self.get_object()
        return Response(snippet.highlighted)


@api_view(["GET"])
def api_root2(request: Request, format: "Optional[str]" = None) -> Response:
    return Response(
        {
            "users": reverse("snippets:users", request=request, format=format),
            # "snippets": reverse("snippet-list", request=request, format=format),
        }
    )

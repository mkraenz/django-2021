from rest_framework import generics, permissions, renderers, serializers, viewsets
from rest_framework.request import Request
from rest_framework.response import Response

from snippets.models import Snippet
from snippets.permissions import IsOwnerOrReadOnly


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    highlight = serializers.HyperlinkedIdentityField(
        view_name="snippet-highlight", format="html"
    )

    def validate_title(self, value: str) -> str:
        if len(value) < 3:
            raise serializers.ValidationError("Must be at least 3 characters long")
        return value

    class Meta:  # type: ignore
        model = Snippet
        fields = [
            "url",
            "id",
            "highlight",
            "title",
            "code",
            "linenos",
            "language",
            "style",
            "owner",
        ]
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

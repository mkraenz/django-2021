from rest_framework import serializers, viewsets

from snippets.models import Snippet


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:  # type: ignore
        model = Snippet
        fields = ["id", "title", "code", "linenos", "language", "style"]


class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

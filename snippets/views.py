from datetime import datetime
from typing import Optional, TypedDict, TypeVar, cast

from rest_framework import serializers, viewsets

from snippets.models import LANGUAGE_CHOICES, STYLE_CHOICES, Snippet

X = TypeVar("X")


def assigned(x: Optional[X]) -> X:
    return cast(X, x)


class SnippetCreate(TypedDict):
    title: "Optional[str]"
    code: str
    linenos: "Optional[bool]"
    language: "Optional[str]"
    style: "Optional[str]"


class SnippetUpdate(TypedDict):
    created: "Optional[datetime]"
    title: "Optional[str]"
    code: "Optional[str]"
    linenos: "Optional[bool]"
    language: "Optional[str]"
    style: "Optional[str]"


class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False)
    code = serializers.CharField(style={"base_template": "textarea.html"})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(LANGUAGE_CHOICES, default="python")
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default="friendly")  # type: ignore

    def create(self, validated_data: SnippetCreate):
        return Snippet.objects.create(**validated_data)

    def update(self, instance: Snippet, validated_data: SnippetUpdate):
        instance.created = assigned(validated_data.get("created", instance.created))
        instance.title = assigned(validated_data.get("title", instance.title))
        instance.code = assigned(validated_data.get("code", instance.code))
        instance.linenos = assigned(validated_data.get("linenos", instance.linenos))
        instance.language = assigned(validated_data.get("language", instance.language))
        instance.style = assigned(validated_data.get("style", instance.style))
        instance.save()
        return instance


class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

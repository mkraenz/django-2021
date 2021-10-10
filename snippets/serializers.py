from django.contrib.auth.models import User
from rest_framework import generics, permissions, serializers

from snippets.models import Snippet


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Snippet.objects.all()
    )

    class Meta:  # type: ignore
        model = User
        fields = ["url", "username", "email", "is_staff", "snippets"]


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserDetails(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

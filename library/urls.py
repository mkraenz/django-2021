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
from django.contrib import admin
from django.contrib.auth.models import User
from django.urls import include, path
from rest_framework import permissions, routers, serializers, viewsets

from books.rest import BookViewSet, ChapterViewSet

from .settings import ADMIN_URL


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:  # type: ignore
        model = User
        fields = [
            "url",
            "username",
            "email",
            "is_staff",
        ]


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register("users", UserViewSet)
router.register("books", BookViewSet)
router.register("chapters", ChapterViewSet)


urlpatterns = [
    path("rest/", include(router.urls)),
    path(ADMIN_URL, admin.site.urls),
    path("books/", include("books.urls")),
    path("i18n/", include("django.conf.urls.i18n")),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]

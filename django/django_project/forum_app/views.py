"""Forum views."""
from django.db.models import Model
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet

from . import serializers
from .models import Message, Section, Thread, User


class MyPermission(BasePermission):
    """Models permission."""

    _safe_methods = 'GET', 'HEAD', 'OPTIONS', 'PATCH', 'POST', 'PUT'
    _unsafe_methods = 'DELETE'

    def has_permission(self, request, _) -> bool:
        """Check user permission.

        Args:
            request (_type_): _description_

        Returns:
            bool: user has the permission true, otherwise false.
        """
        if request.method in self._safe_methods and self._is_authenticated(request):
            return True
        elif request.method in self._unsafe_methods and self._is_superuser(request):
            return True
        return False

    def _is_authenticated(self, request):
        return request.user and request.user.is_authenticated

    def _is_superuser(self, request):
        return request.user and request.user.is_superuser


def create_viewset(model_class: Model, serializer: ModelSerializer):
    """Create view set class by models_class and serializer.

    Args:
        model_class (Model): class model.
        serializer (ModelSerializer): model serializer.

    Returns:
        CustomViewSet: base view set of model and serializer.
    """
    class CustomViewSet(ModelViewSet):
        """Base view set."""

        serializer_class = serializer
        queryset = model_class.objects.all()
        permission_classes = [MyPermission]
        authentication_classes = [TokenAuthentication]

    return CustomViewSet


class ThreadViewSet(ModelViewSet):
    """Thread view set."""

    serializer_class = serializers.ThreadSerializer
    queryset = Thread.objects.all()
    permission_classes = [MyPermission]
    authentication_classes = [TokenAuthentication]

    def list(self, request: Request, pk: str | None = None) -> Response:
        """Get list of threads.

        Args:
            request (Request): request.
            pk (str | None, optional): identifier. Defaults to None.

        Returns:
            Response: list of thread. Filter by query 'sectionId'.
        """
        if pk is not None:
            threads = Thread.objects.get(id=pk)
        else:
            section_id = request.query_params.get('sectionId')
            if section_id:
                sections = list(Section.objects.filter(id=section_id))
                if not sections:
                    return Response(status=status.HTTP_404_NOT_FOUND)
                threads = sections[0].threads
            else:
                threads = Thread.objects.all()
        serializer = self.get_serializer(threads, many=True)
        result_set = serializer.data

        return Response(result_set)


UserViewSet = create_viewset(User, serializers.UserSerializerDAB)
SectionViewSet = create_viewset(Section, serializers.SectionSerializer)
MessageViewSet = create_viewset(Message, serializers.MessageSerializer)

"""Forum views."""
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import BasePermission
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from . import serializers
from .models import Message, Section, Thread, User


class MyPermission(BasePermission):
    _safe_methods = 'GET', 'HEAD', 'OPTIONS', 'PATCH', 'POST', 'PUT'
    _unsafe_methods = 'DELETE'

    def is_authenticated(self, request):
        return request.user and request.user.is_authenticated

    def is_superuser(self, request):
        return request.user and request.user.is_superuser

    def has_permission(self, request, _):
        if request.method in self._safe_methods and self.is_authenticated(request):
            return True
        elif request.method in self._unsafe_methods and self.is_superuser(request):
            return True
        return False


def create_viewset(model_class, serializer):
    class CustomViewSet(ModelViewSet):
        serializer_class = serializer
        queryset = model_class.objects.all()
        permission_classes = [MyPermission]
        authentication_classes = [TokenAuthentication]

    return CustomViewSet


class ThreadViewSet(ModelViewSet):
    serializer_class = serializers.ThreadSerializer
    queryset = Thread.objects.all()
    permission_classes = [MyPermission]
    authentication_classes = [TokenAuthentication]

    def list(self, request, pk=None):
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

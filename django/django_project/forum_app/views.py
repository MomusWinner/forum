from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import BasePermission
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import UserSerializerDAB, ThreadSerializer, SectionSerializer, MessageSerializer
from .models import User, Thread, Section, Message


class MyPermission(BasePermission): #TODO Change permission
    _safe_methods = 'GET', 'HEAD', 'OPTIONS', 'PATCH', 'POST', 'PUT',
    _unsafe_methods = 'DELETE'

    def has_permission(self, request, _):
        if request.method in self._safe_methods and (request.user and request.user.is_authenticated):
            return True
        if request.method in self._unsafe_methods and (request.user and request.user.is_superuser):
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
    serializer_class = ThreadSerializer
    queryset = Thread.objects.all()
    permission_classes = [MyPermission]
    authentication_classes = [TokenAuthentication]

    def list(self, request, pk=None):
        if pk != None:
            threads =  Thread.objects.get(id=pk)
        else:
            sectionId = request.query_params.get('sectionId')
            if sectionId:
                threads = list(Section.objects.filter(id=sectionId))[0].threads
            else:
                threads = Thread.objects.all()


        serializer = self.get_serializer(threads, many=True)
        result_set = serializer.data

        return Response(result_set)


UserViewSet = create_viewset(User, UserSerializerDAB)
SectionViewSet = create_viewset(Section, SectionSerializer)
MessageViewSet = create_viewset(Message, MessageSerializer)
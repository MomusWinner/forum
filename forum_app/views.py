from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import BasePermission
from rest_framework.authentication import TokenAuthentication

from .forms import RegistrationForm
from .serializers import UserSerializer, ThreadSerializer, SectionSerializer, MessageSerializer
from .models import User, Thread, Section, Message


class MyPermission(BasePermission): #TODO Change permission
    _safe_methods = 'GET', 'HEAD', 'OPTIONS', 'PATCH'
    _unsafe_methods = 'POST', 'PUT', 'DELETE'

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


def register(request):
    errors = ''
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            User.objects.create(user=user)
        else:
            errors = form.errors
    else:
        form = RegistrationForm()

    return render(
        request,
        'registration/register.html',
        {
            'form': form,
            'errors': errors,
        }
    )

ThreadViewSet = create_viewset(Thread, ThreadSerializer)
SectionViewSet = create_viewset(Section, SectionSerializer)
MessageViewSet = create_viewset(Message, MessageSerializer)
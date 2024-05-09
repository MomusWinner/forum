from .models import User, Thread, Section, Message
from rest_framework.serializers import HyperlinkedModelSerializer


class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ThreadSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Thread
        fields = '__all__'


class SectionSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'


class MessageSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

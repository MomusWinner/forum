from .models import User, Thread, Section, Message
from rest_framework.serializers import HyperlinkedModelSerializer, PrimaryKeyRelatedField


class UserSerializerDAB(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class ThreadSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Thread
        fields = ('id', 'title', 'user_id', 'created')


class SectionSerializer(HyperlinkedModelSerializer):
    threads = PrimaryKeyRelatedField(queryset=Thread.objects.all(), many=True)

    class Meta:
        model = Section
        fields = ('id', 'name', 'threads')


class MessageSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'thread_id', 'user_id', 'message_body', 'created')

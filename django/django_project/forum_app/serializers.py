"""Forum serializers."""
from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField

from .models import Message, Section, Thread, User


class SectionSerializer(ModelSerializer):
    threads = PrimaryKeyRelatedField(queryset=Thread.objects.all(), many=True)

    class Meta:
        model = Section
        fields = ('id', 'name', 'threads')


class MessageSerializer(ModelSerializer):
    def create(self, validated_data):
        user = self.context['request'].user
        return Message.objects.create(
            user=user,
            **validated_data,
        )

    class Meta:
        model = Message
        fields = ('id', 'thread', 'user', 'message_body', 'created')


class ThreadSerializer(ModelSerializer):
    messages = MessageSerializer(read_only=True, many=True, source='message_set')
    sections = PrimaryKeyRelatedField(queryset=Section.objects.all(), many=True)

    def create(self, validated_data):
        user = self.context['request'].user
        thread_data = {
            key: thread_value for key, thread_value in validated_data.items() if key != 'sections'
        }
        thread = Thread.objects.create(
            user=user,
            **thread_data,
        )
        thread.sections.set([section.id for section in validated_data['sections']])
        return thread

    class Meta:
        model = Thread
        fields = ('id', 'title', 'user_id', 'sections', 'created', 'messages')


class UserSerializerDAB(ModelSerializer):
    threads = ThreadSerializer(read_only=True, many=True, source='thread_set')

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'threads')

from .models import User, Thread, Section, Message
from rest_framework.serializers import HyperlinkedModelSerializer, PrimaryKeyRelatedField, ModelSerializer


class UserSerializerDAB(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class SectionSerializer(HyperlinkedModelSerializer):
    threads = PrimaryKeyRelatedField(queryset=Thread.objects.all(), many=True)

    class Meta:
        model = Section
        fields = ('id', 'name', 'threads')

class MessageSerializer(ModelSerializer):
    def create(self, validated_data):
        user = self.context['request'].user
        print(user)
        message = Message.objects.create(
            user=user,
            **validated_data
        )

        return message

    class Meta:
        model = Message
        fields = ('id', 'thread', 'user', 'message_body', 'created')


class ThreadSerializer(ModelSerializer):
    messages = MessageSerializer(read_only=True, many=True, source='message_set', )
    sections = PrimaryKeyRelatedField(queryset=Section.objects.all(), many=True)

    def create(self, validated_data):
        user = self.context['request'].user
        data = {key: value for key, value in validated_data.items() if key != 'sections'}
        thread = Thread.objects.create(
            user=user,
            **data
        )
        thread.sections.set([section.id for section in validated_data['sections']])
        return thread

    class Meta:
        model = Thread
        fields = ('id', 'title', 'user_id', 'sections', 'created', 'messages')

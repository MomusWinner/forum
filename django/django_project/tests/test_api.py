from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token
from random import randint
from forum_app.models import User, Message, Thread, Section

API = '/api/v1/'

class MessageTest(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.url = API + 'message/'

        self.thread = Thread.objects.create(title="test_thread")
        self.user = User.objects.create(username='user_test', password='test')
        self.superuser = User.objects.create(
            username='admin_test', password='test', is_superuser=True,
        )

        self.user_token = Token(user=self.user)
        self.superuser_token = Token(user=self.superuser)

    def manage(
        self,
        user: User,
        token: Token,
        post_expected: int,
        put_expected: int,
        delete_expected: int,
        ):
            self.client.force_authenticate(user=user, token=token)

            self.assertEqual(self.client.get(self.url).status_code, status.HTTP_200_OK)
            self.assertEqual(self.client.head(self.url).status_code, status.HTTP_200_OK)
            self.assertEqual(self.client.options(self.url).status_code, status.HTTP_200_OK)

            post_put_data = {"message_body": "<p>test messgae</p>", "thread": self.thread.id}
            self.assertEqual(self.client.post(self.url, post_put_data).status_code, post_expected)
            created_id = Message.objects.create(message_body="<p>test_message</p>", thread=self.thread).id
            instance_url = f'{self.url}{created_id}/'

            put_response = self.client.put(instance_url, post_put_data)
            self.assertEqual(put_response.status_code, put_expected)

            delete_response = self.client.delete(instance_url, {})
            self.assertEqual(delete_response.status_code, delete_expected)

    def test_superuser(self):
        self.manage(
            self.superuser, self.superuser_token,
            post_expected=status.HTTP_201_CREATED,
            put_expected=status.HTTP_200_OK,
            delete_expected=status.HTTP_204_NO_CONTENT,
        )

    def test_user(self):
        self.manage(
            self.user, self.user_token,
            post_expected=status.HTTP_201_CREATED,
            put_expected=status.HTTP_200_OK,
            delete_expected=status.HTTP_403_FORBIDDEN,
        )
class ThreadTest(TestCase):
    def setUp(self) -> None:
        self.post_put_data = {"title": "some book", "sections" : []}
        self.client = APIClient()
        self.url = API+'thread/'

        self.user = User.objects.create(username='user_test', password='test')
        self.superuser = User.objects.create(
            username='admin_test', password='test', is_superuser=True,
        )

        self.user_token = Token(user=self.user)
        self.superuser_token = Token(user=self.superuser)

    def manage(
        self, user: User, token: Token,
        post_expected: int,
        put_expected: int,
        delete_expected: int,
        ):
            self.client.force_authenticate(user=user, token=token)

            self.assertEqual(self.client.get(self.url).status_code, status.HTTP_200_OK)
            self.assertEqual(self.client.head(self.url).status_code, status.HTTP_200_OK)
            self.assertEqual(self.client.options(self.url).status_code, status.HTTP_200_OK)
            self.assertEqual(self.client.post(self.url, self.post_put_data).status_code, post_expected)
            created_id = Thread.objects.create(title="some").id
            instance_url = f'{self.url}{created_id}/'
            put_response = self.client.put(instance_url, self.post_put_data)
            self.assertEqual(put_response.status_code, put_expected)

            delete_response = self.client.delete(instance_url, {})
            self.assertEqual(delete_response.status_code, delete_expected)

    def test_superuser(self):
        self.manage(
            self.superuser, self.superuser_token,
            post_expected=status.HTTP_201_CREATED,
            put_expected=status.HTTP_200_OK,
            delete_expected=status.HTTP_204_NO_CONTENT,
        )

    def test_user(self):
        self.manage(
            self.user, self.user_token,
            post_expected=status.HTTP_201_CREATED,
            put_expected=status.HTTP_200_OK,
            delete_expected=status.HTTP_403_FORBIDDEN,
        )


class SectionTest(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.url = API + 'section/'

        self.user = User.objects.create(username='user_test', password='test')
        self.superuser = User.objects.create(
            username='admin_test', password='test', is_superuser=True,
        )

        self.user_token = Token(user=self.user)
        self.superuser_token = Token(user=self.superuser)

    def manage(
        self,
        section_name: str,
        user: User,
        token: Token,
        post_expected: int,
        put_expected: int,
        delete_expected: int,
        ):
            self.client.force_authenticate(user=user, token=token)

            self.assertEqual(self.client.get(self.url).status_code, status.HTTP_200_OK)
            self.assertEqual(self.client.head(self.url).status_code, status.HTTP_200_OK)
            self.assertEqual(self.client.options(self.url).status_code, status.HTTP_200_OK)

            post_data = {'name': 'test_section_post_'+str(user.id), 'threads': []}
            self.assertEqual(self.client.post(self.url, post_data).status_code, post_expected)
            created_id = Section.objects.create(name=section_name).id
            instance_url = f'{self.url}{created_id}/'

            put_data = {'name': 'test_section_put_'+str(user.id), 'threads': []}
            put_response = self.client.put(instance_url, put_data)
            self.assertEqual(put_response.status_code, put_expected)

            delete_response = self.client.delete(instance_url, {})
            self.assertEqual(delete_response.status_code, delete_expected)

    def test_superuser(self):
        self.manage(
            "some_section_supper_user",
            self.superuser, self.superuser_token,
            post_expected=status.HTTP_201_CREATED,
            put_expected=status.HTTP_200_OK,
            delete_expected=status.HTTP_204_NO_CONTENT,
        )

    def test_user(self):
        self.manage(
             "some_section_user",
            self.user, self.user_token,
            post_expected=status.HTTP_201_CREATED,
            put_expected=status.HTTP_200_OK,
            delete_expected=status.HTTP_403_FORBIDDEN,
        )
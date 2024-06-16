"""API tests."""
from django.test import TestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from forum_app.models import Message, Section, Thread, User

API = '/api/v1/'


def get_user() -> User:
    return User.objects.create(username='user_test', password='test')


def get_superuser() -> User:
    return User.objects.create(username='admin_test', password='test', is_superuser=True)


class MessageTest(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.url = f'{API}message/'

        self._thread = Thread.objects.create(title='test_thread')
        self._user, self._superuser = get_user(), get_superuser()
        self._user_token = Token(user=self._user)
        self._superuser_token = Token(user=self._superuser)

    def manage(
        self,
        user: User,
        token: Token,
        delete_expected: int,
    ) -> None:
        self.client.force_authenticate(user=user, token=token)

        self.assertEqual(self.client.get(self.url).status_code, status.HTTP_200_OK)
        self.assertEqual(self.client.head(self.url).status_code, status.HTTP_200_OK)
        self.assertEqual(self.client.options(self.url).status_code, status.HTTP_200_OK)

        post_put_data = {'message_body': 'test messgae', 'thread': self._thread.id}
        self.assertEqual(
            self.client.post(self.url, post_put_data).status_code, status.HTTP_201_CREATED,
        )
        created_id = Message.objects.create(message_body='test_message', thread=self._thread).id
        instance_url = f'{self.url}{created_id}/'

        put_response = self.client.put(instance_url, post_put_data)
        self.assertEqual(put_response.status_code, status.HTTP_200_OK)

        delete_response = self.client.delete(instance_url, {})
        self.assertEqual(delete_response.status_code, delete_expected)

    def test_superuser(self) -> None:
        self.manage(
            self._superuser, self._superuser_token,
            delete_expected=status.HTTP_204_NO_CONTENT,
        )

    def test_user(self) -> None:
        self.manage(
            self._user, self._user_token,
            delete_expected=status.HTTP_403_FORBIDDEN,
        )


class ThreadTest(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.url = f'{API}thread/'

        self._post_put_data = {'title': 'test_thread', 'sections': []}
        self._user, self._superuser = get_user(), get_superuser()
        self._user_token = Token(user=self._user)
        self._superuser_token = Token(user=self._superuser)

    def manage(
        self, user: User, token: Token,
        delete_expected: int,
    ) -> None:
        self.client.force_authenticate(user=user, token=token)
        self.assertEqual(self.client.get(self.url).status_code, status.HTTP_200_OK)
        self.assertEqual(self.client.head(self.url).status_code, status.HTTP_200_OK)
        self.assertEqual(self.client.options(self.url).status_code, status.HTTP_200_OK)
        self.assertEqual(
            self.client.post(self.url, self._post_put_data).status_code, status.HTTP_201_CREATED,
        )
        created_id = Thread.objects.create(title='some').id
        instance_url = f'{self.url}{created_id}/'
        put_response = self.client.put(instance_url, self._post_put_data)
        self.assertEqual(put_response.status_code, status.HTTP_200_OK)

        delete_response = self.client.delete(instance_url, {})
        self.assertEqual(delete_response.status_code, delete_expected)

    def test_superuser(self) -> None:
        self.manage(
            self._superuser, self._superuser_token,
            delete_expected=status.HTTP_204_NO_CONTENT,
        )

    def test_user(self):
        self.manage(
            self._user, self._user_token,
            delete_expected=status.HTTP_403_FORBIDDEN,
        )


class SectionTest(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.url = f'{API}section/'

        self._user, self._superuser = get_user(), get_superuser()
        self._user_token = Token(user=self._user)
        self._superuser_token = Token(user=self._superuser)

    def manage(
        self,
        section_name: str,
        user: User,
        token: Token,
        delete_expected: int,
    ) -> None:
        self.client.force_authenticate(user=user, token=token)

        self.assertEqual(self.client.get(self.url).status_code, status.HTTP_200_OK)
        self.assertEqual(self.client.head(self.url).status_code, status.HTTP_200_OK)
        self.assertEqual(self.client.options(self.url).status_code, status.HTTP_200_OK)

        post_data = {'name': f'test_section_post_{str(user.id)}', 'threads': []}
        self.assertEqual(
            self.client.post(self.url, post_data).status_code, status.HTTP_201_CREATED,
        )
        created_id = Section.objects.create(name=section_name).id
        instance_url = f'{self.url}{created_id}/'

        put_data = {'name': f'test_section_put_{str(user.id)}', 'threads': []}
        put_response = self.client.put(instance_url, put_data)
        self.assertEqual(put_response.status_code, status.HTTP_200_OK)

        delete_response = self.client.delete(instance_url, {})
        self.assertEqual(delete_response.status_code, delete_expected)

    def test_superuser(self) -> None:
        self.manage(
            'some_section_supper_user',
            self._superuser, self._superuser_token,
            post_expected=status.HTTP_201_CREATED,
            put_expected=status.HTTP_200_OK,
            delete_expected=status.HTTP_204_NO_CONTENT,
        )

    def test_user(self) -> None:
        self.manage(
            'some_section_user',
            self._user, self._user_token,
            post_expected=status.HTTP_201_CREATED,
            put_expected=status.HTTP_200_OK,
            delete_expected=status.HTTP_403_FORBIDDEN,
        )

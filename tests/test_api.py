from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token

from forum_app.models import User, Message, Thread, Section

def create_api_test(model, url, get_creation_attrs):
    class ApiTest(TestCase):
        def setUp(self) -> None:
            self.creation_attrs = get_creation_attrs()
            self.client = APIClient()

            self.user = User.objects.create(username='user_test', password='test')
            self.superuser = User.objects.create(
                username='admin_test', password='test', is_superuser=True,
            )

            # creating tokens for users
            self.user_token = Token(user=self.user)
            self.superuser_token = Token(user=self.superuser)

        def manage(
            self, user: User, token: Token,
            post_expected: int,
            put_expected: int,
            delete_expected: int,
        ):
            self.client.force_authenticate(user=user, token=token)

            self.assertEqual(self.client.get(url).status_code, status.HTTP_200_OK)
            self.assertEqual(self.client.head(url).status_code, status.HTTP_200_OK)
            self.assertEqual(self.client.options(url).status_code, status.HTTP_200_OK)

            self.assertEqual(self.client.post(url, self.creation_attrs).status_code, post_expected)
            
            created_id = model.objects.create(**self.creation_attrs).id
            instance_url = f'{url}{created_id}/'
            put_response = self.client.put(instance_url, self.creation_attrs)
            self.assertEqual(put_response.status_code, put_expected)

            delete_response = self.client.delete(instance_url, self.creation_attrs)
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
                post_expected=status.HTTP_403_FORBIDDEN,
                put_expected=status.HTTP_403_FORBIDDEN,
                delete_expected=status.HTTP_403_FORBIDDEN,
            )
    return ApiTest

url = '/api/'
ThreadApiTest = create_api_test(Thread, f'{url}thread/', lambda : {'title': 'string'})
#MessageApiTest = create_api_test(Message,  f'{url}message/', lambda  : { 'message_body': 'Hello world', 'thread': Thread.objects.create(title='some')})
SectionApiTest = create_api_test(Section, f'{url}section/', lambda : {'name': 'test_section'})
from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework import status

from .models import Transaction

User = get_user_model()


class UserListTest(TestCase):

    def setUp(self) -> None:
        self.user1 = User.objects.create(
            username='customer1',
            password='123',
            role=User.CUSTOMER,
            balance=2000
        )

        self.user2 = User.objects.create(
            username='executor1',
            password='123',
            role=User.EXECUTOR,
            balance=200
        )

    def get_list_users_test(self):
        url = 'http://127.0.0.1:8000/api/v1/users/'

        test = self.client.get(url)

        self.assertEqual(test.status_code, status.HTTP_401_UNAUTHORIZED)


class UserSignUpTest(TestCase):

    def test_sign_up(self):
        url = 'http://127.0.0.1:8000/api/v1/sign_up/'
        data={
            'username': 'test', 'password': '123',
            'first_name': 'qwerty', 'last_name': 'qwerty',
            'email': 'test@gmail.com', 'role': 1, 'balance': 500
        }

        test = self.client.post(url, data)

        self.assertEqual(test.status_code, status.HTTP_201_CREATED)

    def test_sign_up_bad_request(self):
        url = 'http://127.0.0.1:8000/api/v1/sign_up/'
        data = {
            'username': 'test',
            'first_name': 'qwerty', 'last_name': 'qwerty',
            'email': 'test@gmail.com', 'role': 1, 'balance': 500
        }

        test = self.client.post(url, data)

        self.assertEqual(test.status_code, status.HTTP_400_BAD_REQUEST)


class UserLoginTest(TestCase):

    def setUp(self) -> None:
        self.user1 = User.objects.create(
            username='customer1',
            password='123',
            role=User.CUSTOMER,
            balance=2000
        )

    def login_test(self):
        url = 'http://127.0.0.1:8000/api/v1/login/'
        data = {
            'username': 'customer1',
            'password': '123'
        }

        test = self.client.post(url, data)

        self.assertEqual(test.status_code, status.HTTP_200_OK)

    def unauthorized_test(self):
        url = 'http://127.0.0.1:8000/api/v1/login/'
        data = {
            'username': 'customer2',
            'password': '123123'
        }

        test = self.client.post(url, data)

        self.assertEqual(test.status_code, status.HTTP_401_UNAUTHORIZED)

    def login_bad_request_test(self):
        url = 'http://127.0.0.1:8000/api/v1/login/'
        test = self.client.post(url,{})

        self.assertEqual(test.status_code, status.HTTP_400_BAD_REQUEST)


class TransactionCreateTest(TestCase):
    def setUp(self) -> None:
        self.user1 = User.objects.create(
            username='customer1',
            password='123',
            role=User.CUSTOMER,
            balance=2000
        )

    def transaction_create_test(self):
        url_task = 'http://127.0.0.1:8000/api/v1/update_balance/'
        data = {
            'user': self.user1.id,
            'reason': Transaction.REPLENISH,
            'amount': 200,
        }
        url_login = 'http://127.0.0.1:8000/api/v1/login/'
        self.client.post(url_login, data={
            'username': 'customer1',
            'password': '123'
        })
        test = self.client.post(url_task, data)

        self.assertEqual(test.status_code,status.HTTP_200_OK)

    def transaction_create_bad_request_test(self):
        url = 'http://127.0.0.1:8000/api/v1/update_balance/'
        data = {
            'user': self.user1.id,
            'reason': Transaction.REPLENISH,
            'datetime': datetime.datetime.now()
        }
        url_login = 'http://127.0.0.1:8000/api/v1/login/'
        self.client.post(url_login, data={
            'username': 'customer1',
            'password': '123'
        })
        test = self.client.post(url, data)

        self.assertEqual(test.status_code, status.HTTP_400_BAD_REQUEST)


class TransactionListTest(TestCase):
    def setUp(self) -> None:
        self.user1 = User.objects.create(
            username='customer1',
            password='123',
            role=User.CUSTOMER,
            balance=2000
        )

        self.user2 = User.objects.create(
            username='executor1',
            password='123',
            role=User.EXECUTOR,
            balance=200
        )

    def get_transaction_history_test(self):
        url = 'http://127.0.0.1:8000/api/v1/balance_history/'

        test = self.client.get(url)

        self.assertEqual(test.status_code, status.HTTP_401_UNAUTHORIZED)
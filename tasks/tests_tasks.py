from django.test import TestCase
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()


class TaskListTest(TestCase):

    def setUp(self):
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

    def get_task_list_unauthorized_test(self):
        url = 'http://0.0.0.0:8000/api/v1/tasks'
        test = self.client.get(url)

        self.assertEqual(test.status_code, status.HTTP_401_UNAUTHORIZED)

    def get_task_list_succes_test(self):
        url_tasks = 'http://0.0.0.0:8000/api/v1/tasks'

        url_login = 'http://0.0.0.0:8000/api/v1/login'
        self.client.post(url_login, data={
            'username': 'customer1',
            'password': '123'
        })

        test = self.client.get(url_tasks)

        self.assertEqual(test.status_code, status.HTTP_200_OK)


class TaskCreateTest(TestCase):

    def setUp(self):
        self.customer= User.objects.create(
            username='customer1',
            password='123',
            role=User.CUSTOMER,
            balance=2000
        )

        self.executor = User.objects.create(
            username='executor1',
            password='123',
            role=User.EXECUTOR,
            balance=200
        )

    def task_create_test(self):
        url_task = 'http://0.0.0.0:8000/api/v1/task'
        data = {
            'title': 'test',
            'description': 'testtesttest',
            'price': 200,
            'executor': self.executor.id,
            'created_by': self.customer.id,
        }
        url_login = 'http://0.0.0.0:8000/api/v1/login'
        self.client.post(url_login, data={
            'username': 'customer1',
            'password': '123'
        })
        test = self.client.post(url_task, data)

        self.assertEqual(test.status_code, status.HTTP_200_OK)

    def task_bad_request_test(self):
        url_task = 'http://0.0.0.0:8000/api/v1/task'
        data = {
            'title': 'test',
            'description': 'testtesttest',
            'price': 200,
            'executor': self.executor.id,
        }
        url_login = 'http://0.0.0.0:8000/api/v1/login'
        self.client.post(url_login, data={
            'username': 'customer1',
            'password': '123'
        })
        test = self.client.post(url_task, data)

        self.assertEqual(test.status_code, status.HTTP_400_BAD_REQUEST)


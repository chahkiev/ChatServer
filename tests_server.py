from django.test import TestCase
import unittest
import json
import requests
from testData.testDataForServer import *


class TestUserAdd(unittest.TestCase):
    create_test_users()
    create_test_chats()
    create_test_messages()
    
    def test_UserAdd_ERROR(self):
        # Invalid data: 'usrnme' instead of 'username'
        url = 'http://localhost:9000/users/add'
        data = '{"usrnme": "test_user_1"}'
        headers = "Content-Type: application/json".split(':')
        headers = {headers[0]: headers[1][1::]}
        r = requests.post(url, data=data, headers=headers)
        self.assertEqual(str(r), '<Response [409]>')

    def test_UserAdd_OK(self):
        url = 'http://localhost:9000/users/add'
        data = '{"username": "test_user_1"}'
        headers = "Content-Type: application/json".split(':')
        headers = {headers[0]: headers[1][1::]}
        r = requests.post(url, data=data, headers=headers)
        self.assertEqual(str(r), '<Response [200]>')


class TestChatsAdd(unittest.TestCase):

    def test_ChatAdd_ERROR(self):
        # Invalid data: 'nme','usrs' instead of 'name','users'
        url = 'http://localhost:9000/chats/add'
        data = {"nme": "test_chat_1", "usrs": [1 , 2]}
        data = json.dumps(data)
        headers = "Content-Type: application/json".split(':')
        headers = {headers[0]: headers[1][1::]}
        r = requests.post(url, data=data, headers=headers)
        self.assertEqual(str(r), '<Response [409]>')

    def test_ChatAdd_OK(self):
        url = 'http://localhost:9000/chats/add'
        data = {"name": "test_chat_2", "users": [3, 4]}
        data = json.dumps(data)
        headers = "Content-Type: application/json".split(':')
        headers = {headers[0]: headers[1][1::]}
        r = requests.post(url, data=data, headers=headers)
        self.assertEqual(str(r), '<Response [200]>')


class TestMessagesAdd(unittest.TestCase):

    def test_MessagesAdd_ERROR(self):
        # Invalid data: 'cht','athr','txt' instead of 'chat','author','text'
        url = 'http://localhost:9000/messages/add'
        data = {"cht": 3, "athr": 5, "txt": "hi"}
        data = json.dumps(data)
        headers = "Content-Type: application/json".split(':')
        headers = {headers[0]: headers[1][1::]}
        r = requests.post(url, data=data, headers=headers)
        self.assertEqual(str(r), '<Response [409]>')


    def test_MessagesAdd_OK(self):
        url = 'http://localhost:9000/messages/add'
        data = {"chat": 4, "author": 7, "text": "hi"}
        data = json.dumps(data)
        headers = "Content-Type: application/json".split(':')
        headers = {headers[0]: headers[1][1::]}
        r = requests.post(url, data=data, headers=headers)
        self.assertEqual(str(r), '<Response [200]>')


class TestChatsGet(unittest.TestCase):

    def test_ChatsGet_ERROR(self):
        # Invalid data: 'usr' instead of 'user'
        url = 'http://localhost:9000/chats/get'
        data = {"usr": 9}
        data = json.dumps(data)
        headers = "Content-Type: application/json".split(':')
        headers = {headers[0]: headers[1][1::]}
        r = requests.post(url, data=data, headers=headers)
        self.assertEqual(str(r), '<Response [409]>')


    def test_ChatsGet_OK(self):
        url = 'http://localhost:9000/chats/get'
        data = {"user": 12}
        data = json.dumps(data)
        headers = "Content-Type: application/json".split(':')
        headers = {headers[0]: headers[1][1::]}
        r = requests.post(url, data=data, headers=headers)
        self.assertEqual(str(r), '<Response [200]>')


class TestMessagesGet(unittest.TestCase):

    def test_MessagesGet_ERROR(self):
        #Invalid data: 'cht' instead of 'chat'
        url = 'http://localhost:9000/messages/get'
        data = {"cht": 9}
        data = json.dumps(data)
        headers = "Content-Type: application/json".split(':')
        headers = {headers[0]: headers[1][1::]}
        r = requests.post(url, data=data, headers=headers)
        self.assertEqual(str(r), '<Response [409]>')


    def test_MessagesGet_OK(self):
        url = 'http://localhost:9000/messages/get'
        data = {"chat": 10}
        data = json.dumps(data)
        headers = "Content-Type: application/json".split(':')
        headers = {headers[0]: headers[1][1::]}
        r = requests.post(url, data=data, headers=headers)
        self.assertEqual(str(r), '<Response [200]>')

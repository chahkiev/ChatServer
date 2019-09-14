import json
import requests
from server.models import User, Chat, ChatUser, Message
from django.utils import timezone

def create_test_users():
    print("Creating testUsers")
    url = 'http://localhost:9000/users/add'
    headers = "Content-Type: application/json".split(':')
    headers = {headers[0]: headers[1][1::]}

    users = ["test_user_1", 
             "test_user_2", 
             "test_user_3", 
             "test_user_4", 
             "test_user_5", 
             "test_user_6", 
             "test_user_7", 
             "test_user_8", 
             "test_user_9", 
             "test_user_10", 
             "test_user_11", 
             "test_user_12", 
             "test_user_13", 
             "test_user_14", 
             "test_user_15", 
             "test_user_16", 
             "test_user_17", 
             "test_user_8"]

    for user in users:
        newUser = User.objects.create(username=str(user),
                                    created_at=timezone.now())
        newUser.save()

    # data = '{"username": "test_user_1"}'
    # r = requests.post(url, data=data, headers=headers)
    # data = '{"username": "test_user_2"}'
    # r = requests.post(url, data=data, headers=headers)
    # data = '{"username": "test_user_3"}'
    # r = requests.post(url, data=data, headers=headers)
    # data = '{"username": "test_user_4"}'
    # r = requests.post(url, data=data, headers=headers)
    # data = '{"username": "test_user_5"}'
    # r = requests.post(url, data=data, headers=headers)
    # data = '{"username": "test_user_6"}'
    # r = requests.post(url, data=data, headers=headers)
    # data = '{"username": "test_user_7"}'
    # r = requests.post(url, data=data, headers=headers)
    # data = '{"username": "test_user_8"}'
    # r = requests.post(url, data=data, headers=headers)
    # data = '{"username": "test_user_9"}'
    # r = requests.post(url, data=data, headers=headers)
    # data = '{"username": "test_user_10"}'
    # r = requests.post(url, data=data, headers=headers)
    # data = '{"username": "test_user_11"}'
    # r = requests.post(url, data=data, headers=headers)
    # data = '{"username": "test_user_12"}'
    # r = requests.post(url, data=data, headers=headers)
    # data = '{"username": "test_user_13"}'
    # r = requests.post(url, data=data, headers=headers)
    # data = '{"username": "test_user_14"}'
    # r = requests.post(url, data=data, headers=headers)
    # data = '{"username": "test_user_14"}'
    # r = requests.post(url, data=data, headers=headers)
    # data = '{"username": "test_user_15"}'
    # r = requests.post(url, data=data, headers=headers)
    # data = '{"username": "test_user_16"}'
    # r = requests.post(url, data=data, headers=headers)
    # data = '{"username": "test_user_17"}'
    # r = requests.post(url, data=data, headers=headers)
    # data = '{"username": "test_user_18"}'
    # r = requests.post(url, data=data, headers=headers)
    return


def create_test_chats():
    print("Creating testChats")
    url = 'http://localhost:9000/chats/add'
    headers = "Content-Type: application/json".split(':')
    headers = {headers[0]: headers[1][1::]}

    chats = [ ["test_chat_3", [5, 6]],
              ["test_chat_4", [7, 8]],
              ["test_chat_5", [9, 10]],
              ["test_chat_6", [9, 11]],
              ["test_chat_7", [12, 13]],
              ["test_chat_8", [13, 14]],
              ["test_chat_9", [15, 16]],
              ["test_chat_10", [17, 18]] ]

    for chat in chats:
        newChat = Chat.objects.create(name=chat[0],
                                    created_at=timezone.now())
        newChat.save()

        for user in chat[1]:
            chatObj = Chat.objects.filter(name=chat[0]).first()
            userObj = User.objects.filter(id=user).first()
            newChatUser = ChatUser.objects.create(chat=chatObj, user=userObj)
            newChatUser.save()

    # data = '{"name": "test_chat_3", "users": [5, 6]}'
    # r = requests.post(url, data=data, headers=headers)
    # data = '{"name": "test_chat_4", "users": [7, 8]}'
    # r = requests.post(url, data=data, headers=headers)
    # data = '{"name": "test_chat_5", "users": [9, 10]}'
    # r = requests.post(url, data=data, headers=headers)
    # data = '{"name": "test_chat_6", "users": [9, 11]}'
    # r = requests.post(url, data=data, headers=headers)
    # data = '{"name": "test_chat_7", "users": [12, 13]}'
    # r = requests.post(url, data=data, headers=headers)
    # data = '{"name": "test_chat_8", "users": [13, 14]}'
    # r = requests.post(url, data=data, headers=headers)
    # data = '{"name": "test_chat_9", "users": [15, 16]}'
    # r = requests.post(url, data=data, headers=headers)
    # data = '{"name": "test_chat_10", "users": [17, 18]}'
    # r = requests.post(url, data=data, headers=headers)
    return


def create_test_messages():
    print("Creating testMessages")
    url = 'http://localhost:9000/messages/add'
    headers = "Content-Type: application/json".split(':')
    headers = {headers[0]: headers[1][1::]}

    messages = [ [9, 15, "hi"],
                 [9, 16, "hello"],
                 [10, 17, "hi"],
                 [10, 18, "hello"] ]

    for message in messages:
        chatObj = Chat.objects.filter(id=message[0]).first()
        userObj = User.objects.filter(id=message[1]).first()
        newMessage = Message.objects.create(chat=chatObj,
                                        author=userObj,
                                        text=message[2],
                                        created_at=timezone.now())
        newMessage.save()

    # data = '{"chat": 9, "author": 15, "text": "hi"}'
    # r = requests.post(url, data=data, headers=headers)
    # data = '{"chat": 9, "author": 16, "text": "hello"}'
    # r = requests.post(url, data=data, headers=headers)
    # data = '{"chat": 10, "author": 17, "text": "hi"}'
    # r = requests.post(url, data=data, headers=headers)
    # data = '{"chat": 10, "author": 18, "text": "hello"}'
    # r = requests.post(url, data=data, headers=headers)
    return


if __name__ == '__main__':
    create_test_users()
    create_test_chats()
    create_test_messages()



# users
# data = '{"username": "test_user_0"}'
# r = requests.post(url, data=data, headers=headers)

# chats
# data = '{"name": "test_chat_1", "users": [1, 2]}'
# r = requests.post(url, data=data, headers=headers)
# data = '{"name": "test_chat_2", "users": [3, 4]}'
# r = requests.post(url, data=data, headers=headers)

#massages
# data = '{"chat": 3, "author": 5, "text": "hi"}'
# r = requests.post(url, data=data, headers=headers)
# data = '{"chat": 4, "author": 7, "text": "hi"}'
# r = requests.post(url, data=data, headers=headers)
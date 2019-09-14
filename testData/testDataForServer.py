import json
from django.utils import timezone
from server.models import User, Chat, ChatUser, Message



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
    return


if __name__ == '__main__':
    create_test_users()
    create_test_chats()
    create_test_messages()

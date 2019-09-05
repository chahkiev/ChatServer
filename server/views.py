import ast
from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from server.models import User, Chat, ChatUser, Message
from django.views.decorators.csrf import csrf_exempt


def user_exists(username):
    user = User.objects.filter(username=username).first()
    if user == None:
        return 0
    else:
        return user.id


def add_users_to_chat(chat, users):
    for userId in users:
        user = User.objects.filter(id=userId).first()
        userExistsInChat = ChatUser.objects.filter(chat=chat, user=userId).first()

        if user != None and userExistsInChat == None:
            chatUserObj = ChatUser.objects.create(chat=chat, user=user)
            chatUserObj.save()
    return


def chat_exists(chatName):
    chat = Chat.objects.filter(name=chatName).first()
    if chat == None:
        return 0
    else:
        return chat.id

    
def add_user(username):
    userExists = user_exists(username)
    if not userExists:
        try:
            userObj = User.objects.create(username=username,
                                    created_at=timezone.now())
            userObj.save()
            userId = User.objects.filter(username=username).first().id
            return {"userId": userId, "status" : 200}
        except:
            return {"userId": None, "status" : 409}
    else:
        return {"userId": userExists, "status" : 200}


def add_chat(chatName, users):
    print('add_chat()')
    chatExists = chat_exists(chatName)
    if not chatExists:
        try:
            chatObj = Chat.objects.create(name=chatName,
                                    created_at=timezone.now())
            chatObj.save()
            chat = Chat.objects.filter(name=chatName).first()
            add_users_to_chat(chat, users)

            return {"chatId": chat.id, "status" : 200}
        except:
            return {"chatId": None, "status" : 409}
    else:
        chat = Chat.objects.filter(name=chatName).first()
        add_users_to_chat(chat, users)
        return {"chatId": chatExists, "status" : 200}


def add_message(chatId, userId, text):
    print('add_message')
    chat = Chat.objects.filter(id=chatId).first()
    author = User.objects.filter(id=userId).first()

    messageObj = Message.objects.create(chat=chat,
                                        author=author,
                                        text=text,
                                        created_at=timezone.now())
    messageObj.save()
    return


def get_chats(userId):
    print('get_chats()')
    chatsUserDB = ChatUser.objects.filter(user=userId)
    chats = []

    for chatUserDB in chatsUserDB:
        chatMessages = Message.objects.filter(chat=chatUserDB.chat).order_by('created_at').reverse()
        for message in chatMessages:
            chats.append( [chatUserDB.chat, message.created_at.created_at.now().strftime("%Y-%m-%d %H:%M:%S")] )
            break

    return


def get_messages(chatId):
    print('get_messages()')
    messagesDB = Message.objects.filter(chat=chatId).order_by('created_at').reverse()
    messages = []

    for message in messagesDB:
        messages.append( [message.chat.name, message.author.username, message.text, message.created_at.now().strftime("%Y-%m-%d %H:%M:%S")] )
    return


@csrf_exempt
def addUser(request):
    body = request.body
    body = body.decode("utf-8")
    data = ast.literal_eval(body)
    print("addUser(),  data: {}".format(data))

    if 'username' in data:
        user = add_user(data['username'])
        return HttpResponse( user["userId"] , status=user["status"])
    else:
        return HttpResponse(status=409)


@csrf_exempt
def addChat(request):
    body = request.body
    body = body.decode("utf-8")
    data = ast.literal_eval(body)
    print("addChat(),  data: {}".format(data))

    if 'name' in data and 'users' in data and data['users'] != []:
        chat = add_chat(data['name'], data['users'])
        return HttpResponse( chat["chatId"] , status=chat["status"])
    else:
        return HttpResponse(status=409)
    

@csrf_exempt
def addMessage(request):
    body = request.body
    body = body.decode("utf-8")
    data = ast.literal_eval(body)
    print("addMessage(),  data: {}".format(data))

    chatExists = Chat.objects.filter(id=data['chat']).first()
    authorExists = User.objects.filter(id=data['author']).first()

    if 'chat' in data and chatExists and \
        'author' in data and authorExists and \
        'text' in data:
            add_message(data['chat'], data['author'], data['text'])
            return HttpResponse(status=200)
    else:
        return HttpResponse(status=409)
    

@csrf_exempt
def getChats(request):
    body = request.body
    body = body.decode("utf-8")
    data = ast.literal_eval(body)
    print("getChats(),  data: {}".format(data))

    if 'user' in data:
        get_chats(data['user'])
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=409)
    return HttpResponse(status=200)


@csrf_exempt
def getMessages(request):
    body = request.body
    body = body.decode("utf-8")
    data = ast.literal_eval(body)
    print("getMessages(),  data: {}".format(data))

    if 'chat' in data:
        get_messages(data['chat'])
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=409)
    return HttpResponse(status=200)
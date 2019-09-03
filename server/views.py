import ast
from django.utils import timezone

from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from server.models import User, Chat, ChatUser, Message
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def print_DB(request):
    print("print_DB()")
    users = User.objects.all()
    for i in users:
        print(i.id, i.username, i.created_at)
    
    print()

    chats = Chat.objects.all()
    for i in chats:
        print(i.id, i.name, i.created_at)

    print()

    chatUser = ChatUser.objects.all()
    for i in chatUser:
        print(i.id, i.chat, i.user)

    print()

    messages = Message.objects.all()
    for i in messages:
        print(i.id, i.chat, i.author, i.text, i.created_at)

    print()

    return HttpResponse(status=200)


def add_user(user):
    print('add_user()')
    userObj = User.objects.create(username=user,
							created_at=timezone.now())
    userObj.save()
    return


def add_chat(chatName, users):
    print('add_chat()')
    chatObj = Chat.objects.create(name=chatName,
							created_at=timezone.now())
    chatObj.save()
    chat = Chat.objects.filter(name=chatName).first()

    #Adding rows without BULK_CREATE
    for userId in users:
        user = User.objects.filter(id=userId).first()
        chatUserObj = ChatUser.objects.create(chat=chat, user=user)
        print(chatUserObj)
        chatUserObj.save()

    #Adding rows with BULK_CREATE
    # usersForCreate = []
    # for userId in users:
    #     user = User.objects.filter(id=userId).first()
    #     chatUserObj = ChatUser.objects.create(chat=chat, user=user)
    #     usersForCreate.append(chatUserObj)

    # print(usersForCreate)
    # ChatUser.objects.bulk_create(usersForCreate, ignore_conflicts=True)

    return


def add_message(chatId, userId, text):
    print('add_message')
    chat = Chat.objects.filter(id=chatId).first()
    author = User.objects.filter(id=userId).first()
    print(chat)
    print(author)
    print(text)
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
            chats.append( [chatUserDB.chat, message.created_at] )
            break

    print(chats)
    return


def get_messages(chatId):
    print('get_messages()')
    return


@csrf_exempt
def addUser(request):
    body = request.body
    print(body)
    body = body.decode("utf-8")
    data = ast.literal_eval(body)
    print(data)
    print(data['username'])

    if 'username' in data:
        add_user(data['username'])
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=409)



@csrf_exempt
def addChat(request):
    body = request.body
    print(body)
    body = body.decode("utf-8")
    data = ast.literal_eval(body)
    print(data)
    print(data['name'])
    print(data['users'])
    if 'name' in data and 'users' in data:
        add_chat(data['name'], data['users'])
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=409)
    


@csrf_exempt
def addMessage(request):
    body = request.body
    print(body)
    body = body.decode("utf-8")
    data = ast.literal_eval(body)
    print(data)
    print(data['chat'])
    print(data['author'])
    print(data['text'])

    if 'chat' in data and 'author' in data and 'text' in data:
        add_message(data['chat'], data['author'], data['text'])
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=409)
    

@csrf_exempt
def getChats(request):
    body = request.body
    print(body)
    body = body.decode("utf-8")
    data = ast.literal_eval(body)
    print(data)
    print(data['user'])

    if 'user' in data:
        get_chats(data['user'])
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=409)
    return HttpResponse(status=200)


@csrf_exempt
def getMessages(request):
    body = request.body
    print(body)
    body = body.decode("utf-8")
    data = ast.literal_eval(body)
    print(data)
    print(data['chat'])

    if 'chat' in data:
        get_messages(data['chat'])
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=409)
    return HttpResponse(status=200)
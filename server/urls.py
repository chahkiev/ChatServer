from django.conf.urls import url
from django.urls import path
from server.views import *

urlpatterns = [
    url(r'^printDB', print_DB, name="print Database"),

    url(r'^users/add', addUser, name="addUser"),

    url(r'^chats/add', addChat, name="addChat"),
    url(r'^messages/add', addMessage, name="addMessage"),

    url(r'^chats/get', getChats, name="getChats"),
    url(r'^messages/get', getMessages, name="getMessages"),
]
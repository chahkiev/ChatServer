from django.db import models
from django.utils import timezone


class User(models.Model):
    username = models.CharField(max_length=50, verbose_name="Username")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="User was created at")

    def __str__(self):
        return self.username


class Chat(models.Model):
    name = models.CharField(max_length=50, verbose_name="Chat_name")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Chat was created at")

    def __str__(self):
        return self.name


class ChatUser(models.Model):
    chat = models.ForeignKey(Chat, verbose_name="Chat Id", on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name="User Id", on_delete=models.CASCADE)


class Message(models.Model):
    chat = models.ForeignKey(Chat, verbose_name="Chat Id", on_delete=models.CASCADE)
    author = models.ForeignKey(User, verbose_name="User Id", on_delete=models.CASCADE)
    text = models.TextField(verbose_name="Message text")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Message was created at")

    def __str__(self):
        return self.text


class Logger(models.Model):
    method = models.TextField(verbose_name="Method")
    data = models.TextField(verbose_name="Data")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Method was requested at")

    def __str__(self):
        return self.method

from django.db import models
from datetime import datetime


class Room(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Message(models.Model):
    value=models.CharField(max_length=1000)
    date=models.DateTimeField(default=datetime.now, blank=False)
    user=models.CharField(max_length=1000)
    room=models.CharField(max_length=200)

    # def __str__(self):
    #     return self.id

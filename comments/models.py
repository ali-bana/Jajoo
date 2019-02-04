from django.db import models

# Create your models here.
from django.forms import CharField, IntegerField


class Comment(models.Model):
    house_id = IntegerField()
    sender_username = CharField(max_length=100)
    comment = CharField(max_length=1000)
from django.db import models
from django.db.models import CharField, IntegerField, ImageField, AutoField

# Create your models here.

class House(models.Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=20)
    owner = CharField(max_length=20)
    rooms = IntegerField()
    beds = IntegerField()
    area = IntegerField()
    max_cap = IntegerField()
    neighbourhood = CharField(max_length=200)
    price_per_night = IntegerField()
    available = CharField(blank=True, max_length=1000)
    base_image = ImageField()
    living_room = ImageField(null=True)
    bed_room = ImageField(null=True)
    kitchen = ImageField(null=True)
    garage = ImageField(null=True)
    outside = ImageField(null=True)
    description = CharField(max_length=10000, default='')
    number_of_reservs = IntegerField(default=0)

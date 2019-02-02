from django.db import models
from django.db.models import CharField, IntegerField, ImageField

# Create your models here.

class House(models.Model):
    name = CharField()
    owner = CharField()
    rooms = IntegerField()
    beds = IntegerField()
    area = IntegerField()
    max_cap = IntegerField()
    price_per_night = IntegerField()
    available = CharField(blank=True)
    base_image = ImageField()
    living_room = ImageField(null=True)
    bed_room = ImageField(null=True)
    kitchen = ImageField(null=True)
    garage = ImageField(null=True)
    outside = ImageField(null=True)

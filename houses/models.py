import json as j
from datetime import datetime as d
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
    outside = ImageField(null=True)
    description = CharField(max_length=10000, default='')
    number_of_reservs = IntegerField(default=0)
    off = IntegerField(default=0)

    def date_to_string(self, date):
        return date.strftime('%Y-%m-%d')

    def string_to_date(self,str):
        return d.strptime(str, '%Y-%m-%d')

    def add_interval(self, data):
        try:
            intervals = j.loads(self.available)['intervals']
        except:
            intervals = []

        intervals.append([self.date_to_string(data['begin']), self.date_to_string(data['end'])])

        self.available = j.dumps({'intervals' : intervals})
        self.save()
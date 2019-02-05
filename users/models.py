from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import EmailField, ImageField, BooleanField, IntegerField
from django.core.validators import RegexValidator


# Create your models here.


class CustomUser(AbstractUser):
    # add additional fields in here
    is_host = BooleanField(default=False)
    email = EmailField(unique=True)

    national_id_validator = RegexValidator(regex=r'\\[0-9]*',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    national_id = models.CharField(validators=[], max_length=10, blank=True, null=True)  # validators should be a list
    image = ImageField(blank=is_host)
    national_id_card = ImageField(blank=is_host)
    popularity = IntegerField(default=0)

    def __str__(self):
        return self.email
from django.db import models
from django.contrib.auth.models import User  # https://docs.djangoproject.com/en/4.2/topics/auth/default/


# Create your models here.
class User(User):
    pass

class Transportation(models.Model):
   TYPE = (
       'bus',
       'car',
       'bike',
       'electric scooter/bike',
       'walk',
   )
   carpool = models.BooleanField(default=False)
   secondhand = models.BooleanField(default=False)
   type = models.CharField(max_length=1, choices=TYPE)
   
class Food(models.Model):
   vegan = models.BooleanField(default=False)
   vegetarian = models.BooleanField(default=False)
   organic = models.BooleanField(default=False)
   MEAT_TYPE = (
       'pork',
       'poultry',
       'beef',
       'seafood'
   )
   meat_type = models.CharField(max_length=1, choices=MEAT_TYPE)
   
class MaterialGoods(models.Model):
    ITEM = (
        'water bottle'
        'reusable bag'
        'technology'
    )
    item = models.CharField(max_length=1, choices=ITEM)
    months_owned = models.IntegerField()
    
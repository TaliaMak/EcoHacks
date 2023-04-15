from django.db import models
from django.contrib.auth.models import User  # https://docs.djangoproject.com/en/4.2/topics/auth/default/


# Create your models here.
class User(User):
    pass

class Transportation(models.Model):
   TYPE = (
       (1, 'bus'),
       (2, 'car'),
       (3, 'bike'),
       (4, 'electric scooter/bike'),
       (5, 'walk'),
   )
   carpool = models.BooleanField(default=False)
   secondhand = models.BooleanField(default=False)
   type = models.CharField(max_length=1, choices=TYPE)
   
class Food(models.Model):
   vegan = models.BooleanField(default=False)
   vegetarian = models.BooleanField(default=False)
   organic = models.BooleanField(default=False)
   MEAT_TYPE = (
       (1, 'pork'),
       (2, 'poultry'),
       (3, 'beef'),
       (4, 'seafood')
   )
   meat_type = models.CharField(max_length=1, choices=MEAT_TYPE)
   
class MaterialGoods(models.Model):
    ITEM = (
        (1, 'water bottle'),
        (2, 'reusable bag'),
        (3, 'technology')
    )
    item = models.CharField(max_length=1, choices=ITEM)
    months_owned = models.IntegerField(default=0)
    

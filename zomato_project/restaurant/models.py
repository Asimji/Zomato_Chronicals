from django.db import models

# Create your models here.
class Dish(models.Model):
    dish_name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=6,decimal_places=2)

class Order(models.Model):
    customer_name=models.CharField(max_length=100)
    dishes=models.ManyToManyField(Dish)
    status=models.CharField(max_length=20,default='received')
        
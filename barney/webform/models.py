from django.db import models

# need to import the receiver to run it...
import webform.receiver

# Create your models here.

class Order(models.Model):
    address = models.TextField(default='')
    plan = models.TextField(default='')
    validated_address = models.TextField(default='')
    sku = models.TextField(default='')

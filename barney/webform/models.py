from django.db import models

# Create your models here.


class Order(models.Model):
    address = models.TextField()
    plan = models.TextField()
    validated_address = models.TextField()
    sku = models.TextField()

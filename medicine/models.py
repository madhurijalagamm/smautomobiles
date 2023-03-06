from django.db import models

class MEDICINE(models.Model):
    quantity = models.IntegerField(default=0)      
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    store = models.CharField(max_length=255)
    instock = models.BooleanField(default=False)
    incart = models.BooleanField(default=False)
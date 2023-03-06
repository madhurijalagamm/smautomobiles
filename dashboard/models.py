from django.db import models

class INVESTIGATOR(models.Model):
    sno = models.IntegerField(default=0)      
    name = models.CharField(max_length=255)
    regid = models.IntegerField(default=0)
    branch = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    mobile = models.IntegerField(default=0)

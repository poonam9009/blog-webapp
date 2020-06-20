from django.contrib.auth.models import User
from django.db import models


class Contacthtmldata(models.Model):
    name = models.CharField(max_length=332, default="")
    email = models.EmailField(default="",max_length=354)
    phone = models.CharField(default="",max_length=343)
    desc = models.TextField(max_length=3467,default="")

    def __str__(self):
        return self.name
    

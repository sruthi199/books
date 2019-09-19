from django.db import models

class Books(models.Model):
   name = models.CharField(max_length=200)
   author = models.CharField(max_length=200)
   price = models.IntegerField(default=0)

#chsnge
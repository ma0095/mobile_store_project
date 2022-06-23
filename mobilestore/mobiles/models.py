from django.db import models

class Mobile(models.Model):
    mob_name=models.CharField(max_length=80)
    brand=models.CharField(max_length=80)
    network=models.CharField(max_length=80)
    price= models.PositiveIntegerField()
    processor=models.CharField(max_length=80)


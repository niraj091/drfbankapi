from django.db import models

class Bank(models.Model):
    ifsc =  models.CharField(primary_key=True,max_length=100)
    bank_id = models.BigIntegerField()
    bank_name = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=50)


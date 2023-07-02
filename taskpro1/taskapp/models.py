from django.db import models


class task(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class task1(models.Model):
    name = models.CharField(max_length=20)
    dob = models.DateField()





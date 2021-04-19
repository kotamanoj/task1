from django.db import models
from django.contrib.auth.models import User


class Register(models.Model):
    username = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.username


class Montly_Expenses(models.Model):
    customer = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    date = models.DateTimeField(null=True)
    description = models.CharField(max_length=80, null=True)
    amount = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.description


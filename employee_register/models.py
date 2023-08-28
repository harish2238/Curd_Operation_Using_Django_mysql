from django.db import models


# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobilenumber = models.CharField(max_length=15)


class Meta:
    db_table = "employees"

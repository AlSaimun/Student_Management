from django.db import models
from .utils import BLOOD_GRP

# Create your models here.
class Year(models.Model):
    year = models.CharField(max_length=3,primary_key=True)
    def __str__(self) -> str:
        return self.year

class Student(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100,unique=True)
    phone_number = models.CharField(max_length=13)
    year = models.ForeignKey(Year,on_delete=models.CASCADE)
    blood_grp = models.CharField(max_length=5,choices=BLOOD_GRP,default='none')

    def __str__(self) -> str:
        return f"{self.id} {self.name} {self.email} {self.year} {self.blood_grp}"

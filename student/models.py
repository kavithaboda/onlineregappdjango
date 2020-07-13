from django.db import models

from adminapp.models import AdminnModel


class StudentModel(models.Model):
    idno=models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50)
    Contactno = models.IntegerField()
    Email = models.EmailField()
    Password = models.CharField(max_length=20)

class EnroleListModel(models.Model):
    studentcontctno = models.IntegerField(null=True)
    courseid = models.IntegerField()#foreign

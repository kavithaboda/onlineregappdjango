from django.db import models

class AdminnModel(models.Model):
    idno = models.AutoField(primary_key=True)#primary
    Coursename=models.CharField(max_length=50,unique=True)
    Faculty=models.CharField(max_length=100)
    Date=models.DateField()
    Time=models.CharField(max_length=50)
    Fee=models.IntegerField()
    Duration=models.CharField(max_length=100)


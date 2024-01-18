from django.db import models

# user -> id(AutoField), name(CharField), gender(CharField), age(IntegerField)
# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()

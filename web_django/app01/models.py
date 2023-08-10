from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=32)

class Script(models.Model):
    id=models.CharField(max_length=32,primary_key=True)
    stars=models.IntegerField(default=0)
from django.db import models

class contact(models.Model):
    Name=models.CharField(max_length=200)
    email=models.EmailField()
    subject=models.CharField(max_length=200)
    message=models.CharField(max_length=200)

# Create your models here.

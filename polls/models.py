from django.db import models

# Create your models here.


class Information(models.Model):
    email  = models.EmailField(max_length = 20)
    phone_number = models.IntegerField()
    name = models.CharField(max_length = 20)
    
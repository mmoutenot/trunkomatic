from django.db import models
from django.contrib.auth.models import User


class Performer(models.Model):
  user = ForeignKey(User)
  ROLE_CHOICES = ['driver','costumes','envelopes','funk','']
  role = models.CharField(choices=ROLE_CHOICES, default='')

# Create your models here.
class Show(models.Model):
  date = models.DateField()
  performers = models.ManyToManyField(Performer)


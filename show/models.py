from django.db import models
from django.contrib.auth.models import User


class Performer(models.Model):
  user = models.ForeignKey(User)
  ROLE_CHOICES = (('DV','driver'),
                  ('CS','costumes'),
                  ('EN','envelopes'),
                  ('FN','funk'),
                  ('',''))
  role = models.CharField(max_length=2, choices=ROLE_CHOICES, default='')

# Create your models here.
class Show(models.Model):
  date = models.DateField()
  performers = models.ManyToManyField(Performer)


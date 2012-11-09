from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
  user = models.ForeignKey(User, related_name='profile')

  phone_number = models.CharField(max_length=10)

  CARRIER_CHOICES = (('VZ','verizon'),
                     ('AT','att'),
                     ('TM','tmobile'),
                     ('SP','sprint'))
  carrier = models.CharField(max_length=2, choices=CARRIER_CHOICES, default='VZ')

  def __unicode__(self):
    return str(self.user)

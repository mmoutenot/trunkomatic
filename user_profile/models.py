from django.contrib.auth.models import User
from django.db import models

from django.contrib.localflavor.us.forms import USPhoneNumberField

class UserProfile(models.Model):
  user = models.ForeignKey(User, related_name='profile')

  phone_number = USPhoneNumberField()

  CARRIER_CHOICES = (('VZ','verizon'),
                     ('AT','att'),
                     ('TM','tmobile'),
                     ('SP','sprint'))
  carrier = models.CharField(max_length=2, choices=CARRIER_CHOICES, default='VZ')

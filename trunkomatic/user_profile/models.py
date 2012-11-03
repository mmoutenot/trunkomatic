from django.contrib.auth.models import User
from django.db import models
from managers import UserProfileManager

from django.contrib.localflabor.us.forms import USPhoneNumberField

class UserProfile(models.Model):
  user = models.ForeignKey(User, related_name='profile')
  objects = UserProfileManager()

  phone_number = USPhoneNumberField()

  CARRIER_CHOICES = ['verizon','att','tmobile','sprint']
  carrier = models.CharField(choices=CARRIER_CHOICES, default='verizon')

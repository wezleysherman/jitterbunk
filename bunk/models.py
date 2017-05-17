# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
import datetime

class User(AbstractUser):
    profile_picture = models.CharField(max_length=200)

class Bunk(models.Model):
    from_user = models.ForeignKey(User, related_name='sent_bunks')
    to_user = models.ForeignKey(User, related_name='received_bunks')
    time = models.DateTimeField(auto_now_add=True)

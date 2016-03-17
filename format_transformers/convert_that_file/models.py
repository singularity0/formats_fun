from __future__ import unicode_literals

from django.db import models
# from django.forms import ModelForm

# Create your models here.
class History(models.Model):
	file_name = models.CharField(max_length = 255)
	date_processed = models.CharField(max_length = 100)
from django.db import models

# Create your models here.
class Spreadsheet(models.Model):
    spreadsheet = models.FileField(upload_to='documents/')
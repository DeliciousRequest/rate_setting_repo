from django.db import models
from .validators import validate_file_extension

# Create your models here.
class Spreadsheet(models.Model):
    spreadsheet = models.FileField(upload_to='documents/', validators=[validate_file_extension])
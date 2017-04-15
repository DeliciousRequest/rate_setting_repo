from django import forms
from .models import Spreadsheet
from django.utils.translation import ugettext_lazy as _

class SpreadsheetForm(forms.ModelForm):
    class Meta:
        model = Spreadsheet
        fields = ('spreadsheet', )
        labels = {
            'spreadsheet': _('')
        }
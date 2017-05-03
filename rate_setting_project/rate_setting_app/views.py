from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.template.context import RequestContext
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from rate_setting_app.rateValidation import *
from rate_setting_app.tableDumps import *

import openpyxl

from .forms import SpreadsheetForm

# Create your views here.
def validation(request):
    if request.method == 'POST':
        form = SpreadsheetForm(request.POST, request.FILES)
        if form.is_valid():
            validation_results = validateSpreadsheet(request.FILES['spreadsheet'])
            form = SpreadsheetForm()
            return render(request, 'rate_setting_app/validation.html', {
                'validation_results': validation_results,
                'form' : form
            })
    else:
        form = SpreadsheetForm()
    return render(request, 'rate_setting_app/validation.html', {
        'form': form
    })
    
def tables(request):
    if request.method == 'POST':
        table_list = populateTableDump(request.POST['tableSelect'])
        return render(request, 'rate_setting_app/tables.html', {
            'table_list': table_list
        })
    return render(request, 'rate_setting_app/tables.html')
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.template.context import RequestContext
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from rate_setting_app.rateValidation import *

import openpyxl

# Create your views here.
    
def validation(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        validation_results = validateSpreadsheet(request.FILES['myfile'])
        return render(request, 'rate_setting_app/validation.html', {
            'validation_results': validation_results,
        })
    return render(request, 'rate_setting_app/validation.html')
    
def tables(request):
    return render(request, 'rate_setting_app/tables.html')
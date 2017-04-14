from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.template.context import RequestContext
from django.conf import settings
from django.core.files.storage import FileSystemStorage

import openpyxl

# Create your views here.
    
def validation(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        wb = openpyxl.load_workbook(request.FILES['myfile'])
        sheet = wb.active
        table_name = sheet['A2'].value + '\n test'
        return render(request, 'rate_setting_app/validation.html', {
            'uploaded_file_url': uploaded_file_url,
            'table_name': table_name
        })
    return render(request, 'rate_setting_app/validation.html')
    
def tables(request):
    return render(request, 'rate_setting_app/tables.html')
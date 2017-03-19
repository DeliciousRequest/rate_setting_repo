from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import loader
from django.template.context import RequestContext
import openpyxl

# Create your views here.
def validation(request):
    return render(request, 'rate_setting_app/validation.html')
    
def tables(request):
    return render(request, 'rate_setting_app/tables.html')

def validate_tables(request):
    error_message = 'Validation will go here.'
    return HttpResponse(error_message)
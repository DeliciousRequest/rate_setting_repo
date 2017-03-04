from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def validation(request):
    return render(request, 'rate_setting_app/validation.html')
    
def tables(request):
    return render(request, 'rate_setting_app/tables.html')
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from django.urls import reverse

import csv

from django.views.generic import TemplateView, ListView

from django.db.models import Q 

def homepage(request):
    
    template = loader.get_template('home.html')
    context = {
        
    }
    return HttpResponse(template.render(context, request))



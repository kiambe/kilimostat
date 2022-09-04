from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from kilimodata.models import Thematic
from django.urls import reverse

from django.views.generic import TemplateView, ListView


def dashboard(request):
    template = loader.get_template('dashboard.html')
    context = {
        
    }
    return HttpResponse(template.render(context, request))



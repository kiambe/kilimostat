import requests

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

import kilimodata
from .models import KilimoDomains
from django.urls import reverse

from django.db.models import Q 
from django.views.generic import TemplateView, ListView


from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


from .serializers import *


# from .filters import FilterKilimoDomains


def index(request):
    
    template = loader.get_template('data.html')
    context = {
        
    }
    return HttpResponse(template.render(context, request))




@api_view(['GET', 'POST'])
def data_list(request):
    if request.method == 'GET':
        data = KilimoData.objects.all()

        serializer = DataSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE'])
def data_detail(request, id):
    try:
        data = KilimoData.objects.get(id=id)
    except KilimoData.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = DataSerializer(kilimodata, kilimodata=request.kilimodata,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
import json
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
from rest_framework.views import APIView


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
        req= request.GET
        data = KilimoData.objects.all()
        if 'county' not in request.GET:
            
            serializer = DataSerializer(data, context={'request': request}, many=True)

            return Response(serializer.data)

        else:
            county = request.GET["county"]
            
            county  = json.loads(county)
            
            data = data.filter(county__in=county)
            
            if 'sector' in req:
                sector = req["sector"]
                sector = json.loads(sector)
                print(sector)
                data = data.filter(sector__in = sector)
            
            if 'subdomain' in req:
                subdomain = req["subdomain"]
                subdomain = json.loads(subdomain)
                
                data = data.filter(subdomain__in = subdomain)
            
            if 'elements' in req:
                elements = req["elements"]
                elements = json.loads(elements)
                
                data = data.filter(elements__in = elements)
            
            serializer = DataSerializer(data, context={'request': request}, many=True).data

            return Response(serializer)
            

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
    


class apputils(APIView):
    def get(self, request):
        

        sectors_data = Sector.objects.order_by("name")
        secotors_ser = SectorSerializer(sectors_data, many=True).data
        
        subdomain_data = Subdomain.objects.order_by("name")
        subdomain_ser = SubdomainSerializer(subdomain_data, many=True).data

        elements_data = Elements.objects.order_by("name")
        elements_ser = ElementsSerializer(elements_data, many=True).data
        
        item_category_data = ItemCategory.objects.order_by("name")
        items_category_ser = ItemCategorySerializer(item_category_data, many=True).data
        
        unit_data = Unit.objects.all()
        unit_ser = UnitSerializer(unit_data, many=True).data
        
        county_data = County.objects.all()
        county_data_ser = CountySerializer(county_data, many=True).data
        
        items_specify = ItemSpecify.objects.all()
        items_specify_ser = ItemSpecifySerializer(items_specify, many=True).data
        
        return Response({
            "sectors":secotors_ser,
            "subdomain":subdomain_ser,
            "element":elements_ser,
            "item_category":items_category_ser,
            "unit":unit_ser,
            "county":county_data_ser,
            "items_specify":items_specify_ser
        })

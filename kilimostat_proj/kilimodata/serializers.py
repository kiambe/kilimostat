from rest_framework import serializers
from .models import *




class SectorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sector 
        fields = "__all__"

class DomainSerializer(serializers.ModelSerializer):

    class Meta:
        model = Domain 
        fields = "__all__"

class SubdomainSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subdomain 
        fields = "__all__"

class CountySerializer(serializers.ModelSerializer):

    class Meta:
        model = County 
        fields = "__all__"

class ElementsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Elements 
        fields = "__all__"


class ItemCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ItemCategory 
        fields = "__all__"


class ItemSpecifySerializer(serializers.ModelSerializer):

    class Meta:
        model = ItemSpecify 
        fields = "__all__"

class UnitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Unit 
        fields = "__all__"


class DataSerializer(serializers.ModelSerializer):
    #sector=SectorSerializer(read_only=True, many=True)
    #subdomain=SubdomainSerializer(read_only=True, many=True)
    #county=CountySerializer(read_only=True, many=True)
    #elements=ElementsSerializer(read_only=True, many=True)
    #itemspecify=ItemSpecifySerializer(read_only=True, many=True)
    #unit=UnitSerializer(read_only=True, many=True)

    class Meta:
        model = KilimoData 
        fields = "__all__"
        depth = 1
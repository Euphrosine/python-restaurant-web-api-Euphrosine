from django.shortcuts import render

from .serializers import DistrictSerializer, SectorSerializer, RestaurantSerializer, DishCategorySerializer, DishSerializer

from .models import District, Sector, Restaurant, DishCategory, Dish, DishImage

from rest_framework.decorators import api_view, permission_classes

from rest_framework.response import Response

from rest_framework import filters
from rest_framework.permissions import IsAuthenticated

# Create your views here.

from rest_framework import generics


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def endPointDocumentation(request):
    routes = [

        {
            'Endpoint': '/searchDistrict/',
            'method': 'GET',
            'body': None,
            'description': 'returns array of all Restaurant in the given District'
        },
        {
            'Endpoint': '/searchSector/',
            'method': 'GET',
            'body': None,
            'description': 'returns array of all Restaurant in the given Sector'
        },
        {
            'Endpoint': '/searchOwner/',
            'method': 'GET',
            'body': None,
            'description': 'returns array of all Restaurant of the given Owner Name (Individual/Company)'
        },
        {
            'Endpoint': '/searchRating/',
            'method': 'GET',
            'body': None,
            'description': 'returns array of all Restaurant of the given Rating'
        },
        {
            'Endpoint': '/searchDish/',
            'method': 'GET',
            'body': None,
            'description': 'returns array of all Dishes and Restaurant of the given Dish Name'
        },

    ]
    return Response(routes)


# Return District Searched

class SearchByDistrict(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)

    search_fields = ['DistrictName']

    filter_backends = (filters.SearchFilter,)

    queryset = District.objects.all()

    serializer_class = DistrictSerializer


# Return Sectors Searched

class SearchBySector(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    search_fields = ['SectorName']
    filter_backends = (filters.SearchFilter,)
    queryset = Sector.objects.all()
    serializer_class = SectorSerializer


# Return Owner (Individual /Company ) Name Searched

class SearchByOwner(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    search_fields = ['owner__username']
    filter_backends = (filters.SearchFilter,)
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


# Return Restaurant with Rating Searched

class searchRating(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    search_fields = ['rating']
    filter_backends = (filters.SearchFilter,)
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


# Return Restaurant with Dishes Searched

class searchDish(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    search_fields = ['DishName']
    filter_backends = (filters.SearchFilter,)
    queryset = Dish.objects.all()
    serializer_class = DishSerializer

# ##############################################################################################


class DistrictList(generics.ListCreateAPIView):

    queryset = District.objects.all()

    serializer_class = DistrictSerializer


class DistrictDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = District.objects.all()

    serializer_class = DistrictSerializer


class SectorList(generics.ListCreateAPIView):

    queryset = Sector.objects.all()

    serializer_class = SectorSerializer


class SectorDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Sector.objects.all()

    serializer_class = SectorSerializer


class RestaurantList(generics.ListCreateAPIView):

    queryset = Restaurant.objects.all()

    serializer_class = RestaurantSerializer


class RestaurantDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Restaurant.objects.all()

    serializer_class = RestaurantSerializer


# DishCategory Section


class DishCategoryList(generics.ListCreateAPIView):

    queryset = DishCategory.objects.all()

    serializer_class = DishCategorySerializer


class DishCategoryDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = DishCategory.objects.all()

    serializer_class = DishCategorySerializer


# Dish Section

class DishList(generics.ListCreateAPIView):

    queryset = Dish.objects.all()

    serializer_class = DishSerializer


class DishDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Dish.objects.all()

    serializer_class = DishSerializer

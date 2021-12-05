from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.contrib.auth.models import User

from .models import District, Sector, Restaurant, DishCategory, Dish, DishImage


class DistrictSerializer(serializers.ModelSerializer):
    Restaurants = serializers.StringRelatedField(many=True)

    class Meta:
        model = District
        fields = ['DistrictName', 'Restaurants']


class SectorSerializer(serializers.ModelSerializer):
    Restaurants = serializers.StringRelatedField(many=True)

    class Meta:
        model = Sector
        fields = ['district','SectorName', 'Restaurants']


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'


class DishCategorySerializer(serializers.ModelSerializer):
    dishcategory = serializers.StringRelatedField(many=True)

    class Meta:
        model = DishCategory
        fields = ['CategoryName', 'dishcategory']


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = '__all__'

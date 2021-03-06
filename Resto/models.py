from django.db import models
from django.contrib.auth.models import User

# Create your models here.

RATING_CHOICE = [
    (1, 'One Star'),
    (2, 'Two Stars'),
    (3, 'Three Stars'),
    (4, 'Four Stars'),
    (5, 'Five Stars'),
]

OWNER_CHOICE = [
    ('INDIVIDUAL', 'Individual'),
    ('COMPANY', 'Company'),
]


class District(models.Model):
    DistrictName = models.CharField(max_length=100)

    def __str__(self):
        return self.DistrictName


class Sector(models.Model):
    district = models.ForeignKey(
        District, on_delete=models.CASCADE, related_name="Sectors")
    SectorName = models.CharField(max_length=100)

    def __str__(self):
        return self.SectorName


class DishCategory(models.Model):
    CategoryName = models.CharField(max_length=100)

    def __str__(self):
        return self.CategoryName


class Restaurant(models.Model):
    RestorantName = models.CharField(max_length=100)
    owner = models.ForeignKey(
        User, related_name='users', on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=OWNER_CHOICE)
    sector = models.ForeignKey(
        Sector, related_name='Restaurants', on_delete=models.CASCADE)
    district = models.ForeignKey(
        District, related_name='Restaurants', on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICE)
    image = models.ImageField(upload_to='images/restaurant/')

    def __str__(self):
        return self.RestorantName


class Dish(models.Model):
    restaurant = models.ForeignKey(
        Restaurant, related_name='restaurant', on_delete=models.CASCADE)
    DishName = models.CharField(max_length=100)
    price = models.IntegerField()
    cooking_time = models.TimeField(auto_now=False, auto_now_add=False)
    ingredient = models.TextField()
    category = models.ForeignKey(
        DishCategory, related_name='dishcategory', on_delete=models.CASCADE)

    def __str__(self):
        return self.DishName


class DishImage(models.Model):
    ImgName = models.ImageField(upload_to='images/dish/')
    dish = models.ForeignKey(
        Dish, related_name='dishimage', on_delete=models.CASCADE)

    def __str__(self):
        return self.ImgName

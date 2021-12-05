from django.urls import path, include
from Resto import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('', views.endPointDocumentation),
    path('login/', obtain_auth_token, name="obtain_auth_token"),
    path('searchDistrict/', views.SearchByDistrict.as_view()),
    path('searchSector/', views.SearchBySector.as_view()),
    path('searchOwner/', views.SearchByOwner.as_view()),
    path('searchRating/', views.searchRating.as_view()),
    path('searchDish/', views.searchDish.as_view()),

    # Authontication urls
    path('auth/', include('djoser.urls')),
    path('auth/users', include('djoser.urls')),
    path('auth/token/login/', include('djoser.urls')),
    path('auth/token/logout/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),


    path('districts/', views.DistrictList.as_view(), name='listDistrict'),
    path('district/<int:pk>', views.DistrictDetail.as_view(), name='listDistrict'),
    path('sectors/', views.SectorList.as_view(), name='listSector'),
    path('sector/<int:pk>', views.SectorDetail.as_view(), name='sectorDetails'),
    path('restaurants/', views.RestaurantList.as_view(), name='listRestorant'),
    path('restaurant/<int:pk>',views.RestaurantDetail.as_view(), name='listRestorant'),
    path('dishCategories/', views.DishCategoryList().as_view(),name='listDishCategories'),
    path('dishes/', views.DishList.as_view(), name='listDishes'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/<int:pk>/', views.Profile.as_view(), name='profile'),
    path('accounts/signup', views.signup, name='signup'),
    path('restaurant/', views.RestaurantList.as_view(), name='restaurant_list'),
    path('restaurant/<int:pk>/', views.RestaurantDetail.as_view(), name='restaurant_detail'),
    path('restaurant/create/', views.RestaurantCreate.as_view(), name='restaurant_create'),
    path('restaurant/<int:pk>/update/', views.RestaurantUpdate.as_view(), name='restaurant_update'),
]
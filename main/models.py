from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=200, blank=False)
    address = models.TextField(blank=False)
    phone = models.TextField(blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=500, blank=True, default='')
    zipcode = models.IntegerField(blank=False)
    
    def __str__(self):
        return f'restaurant name - {self.name}'
    
    def get_absolute_url(self):
        return reverse('restaurant_detail', kwargs={'pk':self.id})

class Menu(models.Model):
    name = models.CharField(max_length=200, blank=False)
    description = models.TextField(max_length=500, blank=True, default='')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return f'menu name - {self.name}'
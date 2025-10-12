from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Car(models.Model):
    CAR_TYPES = [
        ('SUV', 'SUV'),
        ('Sedan', 'Sedan'),
        ('Hatchback', 'Hatchback'),
        ('Coupe', 'Coupe'),
        ('Convertible', 'Convertible'),
        ('Truck', 'Truck'),
        ('Van', 'Van'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    car_type = models.CharField(max_length=20, choices=CAR_TYPES, default='Sedan')
    description = models.TextField()
    image = models.ImageField(upload_to='car_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    is_sold = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.year} {self.brand} {self.model}"
    
    def get_absolute_url(self):
        return reverse('car-detail', kwargs={'pk': self.pk})
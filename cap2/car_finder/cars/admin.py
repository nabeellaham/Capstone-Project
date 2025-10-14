from django.contrib import admin
from .models import Car

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['brand', 'model', 'year', 'price', 'user', 'is_sold', 'created_at',]
    list_filter = ['brand', 'car_type', 'is_sold', 'created_at']
    search_fields = ['brand', 'model', 'user__username']
    
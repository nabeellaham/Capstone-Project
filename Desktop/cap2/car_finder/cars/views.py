from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Car
from .forms import CarForm

def home(request):
    cars = Car.objects.filter(is_sold=False)
    
    brand = request.GET.get('brand')
    model = request.GET.get('model')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    car_type = request.GET.get('car_type')
    
    if brand:
        cars = cars.filter(brand__icontains=brand)
    if model:
        cars = cars.filter(model__icontains=model)
    if min_price:
        cars = cars.filter(price__gte=min_price)
    if max_price:
        cars = cars.filter(price__lte=max_price)
    if car_type:
        cars = cars.filter(car_type=car_type)
    
    context = {
        'cars': cars,
        'car_types': Car.CAR_TYPES,
    }
    return render(request, 'cars/home.html', context)

def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    context = {'car': car}
    return render(request, 'cars/car_detail.html', context)

@login_required
def my_listings(request):
    cars = Car.objects.filter(user=request.user)
    context = {'cars': cars}
    return render(request, 'cars/my_listings.html', context)

@login_required
def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            car = form.save(commit=False)
            car.user = request.user
            car.save()
            messages.success(request, 'Car listing created successfully!')
            return redirect('my-listings')
    else:
        form = CarForm()
    return render(request, 'cars/car_form.html', {'form': form, 'title': 'Add Car'})

@login_required
def edit_car(request, pk):
    car = get_object_or_404(Car, pk=pk)
    
    if car.user != request.user:
        messages.error(request, 'You can only edit your own listings!')
        return redirect('home')
    
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            form.save()
            messages.success(request, 'Car listing updated successfully!')
            return redirect('my-listings')
    else:
        form = CarForm(instance=car)
    return render(request, 'cars/car_form.html', {'form': form, 'title': 'Edit Car'})

@login_required
def delete_car(request, pk):
    car = get_object_or_404(Car, pk=pk)
    
    if car.user != request.user:
        messages.error(request, 'You can only delete your own listings!')
        return redirect('home')
    
    if request.method == 'POST':
        car.delete()
        messages.success(request, 'Car listing deleted successfully!')
        return redirect('my-listings')
    
    return render(request, 'cars/confirm_delete.html', {'car': car})
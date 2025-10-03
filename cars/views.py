from django.shortcuts import render, get_object_or_404, redirect
from .models import Car, Brand
from .forms import OrderForm, CarForm
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required

def car_list(request):
    """Основная страница со списком авто"""
    brands = Brand.objects.all()
    return render(request, 'cars/car_list.html', {'brands': brands})

def car_filter(request):
    """Фильтрация (AJAX)"""
    qs = Car.objects.filter(status='available').select_related('brand')

    q = request.GET.get('q')
    brand = request.GET.get('brand')
    price_min = request.GET.get('price_min')
    price_max = request.GET.get('price_max')
    year_min = request.GET.get('year_min')
    year_max = request.GET.get('year_max')

    if q:
        qs = qs.filter(
            Q(model__icontains=q) |
            Q(description__icontains=q) |
            Q(brand__name__icontains=q)
        )
    if brand:
        qs = qs.filter(brand__id=brand)
    if price_min:
        qs = qs.filter(price__gte=price_min)
    if price_max:
        qs = qs.filter(price__lte=price_max)
    if year_min:
        qs = qs.filter(year__gte=year_min)
    if year_max:
        qs = qs.filter(year__lte=year_max)

    paginator = Paginator(qs.order_by('-created_at'), 12)
    page = request.GET.get('page')
    cars = paginator.get_page(page)

    return render(request, 'cars/car_list_results.html', {'cars': cars})


def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.car = car
            if request.user.is_authenticated:
                order.buyer = request.user
            order.save()
            return redirect('cars:order_thanks')
    else:
        form = OrderForm()
    return render(request, 'cars/car_detail.html', {'car': car, 'form': form})

def order_thanks(request):
    return render(request, 'cars/order_thanks.html')

def car_buy(request, pk):
    car = get_object_or_404(Car, pk=pk)
    return render(request, 'cars/car_buy.html', {'car': car})

@login_required
def car_add(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            car = form.save(commit=False)
            car.owner = request.user
            car.save()
            return redirect('cars:car_list')
    else:
        form = CarForm()
    return render(request, 'cars/car_add.html', {'form': form})


@login_required(login_url='login_user')
def my_cars(request):
    cars = Car.objects.filter(owner=request.user)
    return render(request, 'cars/my_cars.html', {'cars': cars})
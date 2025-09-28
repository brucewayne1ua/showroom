from django.shortcuts import render, get_object_or_404, redirect
from .models import Car, Brand
from .forms import OrderForm, CarForm
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required

def car_list(request):
    qs = Car.objects.filter(status='available').select_related('brand')
    q = request.GET.get('q')
    brand = request.GET.get('brand')
    if q:
        qs = qs.filter(Q(model__icontains=q) | Q(description__icontains=q) | Q(brand__name__icontains=q))
    if brand:
        qs = qs.filter(brand__id=brand)
    paginator = Paginator(qs.order_by('-created_at'), 12)
    page = request.GET.get('page')
    cars = paginator.get_page(page)
    brands = Brand.objects.all()
    return render(request, 'cars/car_list.html', {'cars': cars, 'brands': brands})

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
            # можно отправить email / уведомление
            return redirect('cars:order_thanks')
    else:
        form = OrderForm()
    return render(request, 'cars/car_detail.html', {'car':car, 'form':form})

def order_thanks(request):
    return render(request, 'cars/order_thanks.html')

def car_buy(request, pk):
    car = get_object_or_404(Car, pk = pk)
    return render(request, 'cars/car_buy.html', {'car': car})

@login_required
def car_add(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            car = form.save(commit=False)
            car.owner = request.user  # привязываем авто к авторизованному юзеру
            car.save()
            return redirect('cars:car_list')
    else:
        form = CarForm()

    return render(request, 'cars/car_add.html', {'form': form})
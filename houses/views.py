from django.shortcuts import render, redirect
from django import forms
from .models import House
from users.models import CustomUser
from .form import HouseRegisterForm, HouseEditForm, HouseAddIntervalForm
from users.models import CustomUser


# Create your views here.

def house_create_view(request):
    if request.user.is_authenticated:
        user = CustomUser.objects.get(email=request.user)
        if request.method == 'POST':
            form = HouseRegisterForm(request.POST, request.FILES or None)
            if form.is_valid():
                obj = House(**form.cleaned_data)
                obj.save()
                return redirect('../%s/details' % obj.id)
        return render(request, 'newHouse.html', {'form': HouseRegisterForm(), 'owner' : user.id})
    return redirect('../../users/login')


def house_add_interval(request, id):
    if request.user.is_authenticated:
        user = CustomUser.objects.get(email=request.user)
        house = House.objects.get(id=id)
        if request.method == 'POST':
            form = HouseAddIntervalForm(request.POST, request.FILES or None)
            if form.is_valid():
                data = form.cleaned_data
                house.add_interval(data)
                return redirect('./details')
        return render(request, 'newInterval.html', {'form': HouseAddIntervalForm()})
    return redirect('../../users/login')


def house_edit_view(request, id):
    try:
        instance = House.objects.get(id=id)
    except:
        return redirect('../../../404')
    if request.method == 'POST':
        form = HouseEditForm(request.POST or None, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('../details')
        else:
            print(form.errors)
            return render(request, 'homeEdit.html', {'form': form})
        return redirect('../../../')
    form = HouseEditForm(instance=instance)
    return render(request, 'homeEdit.html', {'form': form})


def house_detail_view(request, id):
    house = House.objects.get(id=id)
    if house is None:
        redirect('../../404')
    else:
        nearby_houses = House.objects.all()
        import json
        intervals = json.loads(house.available)['intervals']
        return render(request, 'homeDetails.html', {'house': house, 'nearby_houses' : nearby_houses, 'intervals':intervals})

def house_search_view(request):
    houses = House.objects.all()
    location = request.GET.get('location')
    sort = request.GET.get('sort')
    capacity = request.GET.get('capacity')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    rooms = request.GET.get('rooms')

    if sort == 'latest':
        houses = houses[::-1]
        pass
    elif sort == 'reserve':
        houses = House.objects.order_by('number_of_reservs')
        pass
    elif sort == 'expensive':
        houses = House.objects.order_by('price_per_night')
        pass
    elif sort == 'cheap':
        houses = House.objects.order_by('price_per_night')
        houses = houses[::-1]
        pass
    if (location != '') and (location is not None):
        t = []
        for h in houses:
            if h.neighbourhood == location:
                t.append(h)
        houses = t

    if (capacity != '') and (capacity is not None):
        capacity = int(capacity)
        t = []
        for h in houses:
            if h.max_cap == capacity:
                t.append(h)
        houses = t

    if (min_price != '') and (min_price is not None):
        min_price = int(min_price)
        t = []
        for h in houses:
            if h.price_per_night >= min_price:
                t.append(h)
        houses = t

    if (max_price != '') and (max_price is not None):
        max_price = int(max_price)
        t = []
        for h in houses:
            if h.price_per_night <= max_price:
                t.append(h)
        houses = t

    if (rooms != '') and (rooms is not None):
        rooms = int(rooms)
        t = []
        for h in houses:
            if h.rooms == rooms:
                t.append(h)
        houses = t

    return render(request, 'houseSearch.html', {'houses': houses,
                                                'n': len(houses)})


def home_page(request):
    latest_houses = House.objects.all()
    latest_houses = latest_houses[::-1]
    populer_houses = House.objects.order_by('number_of_reservs').all()
    popular_hosts = CustomUser.objects.order_by('popularity').all()


    return render(request, 'index.html', {
        'latest': latest_houses,
        'popular_houses': populer_houses,
        'popular_hosts': popular_hosts
    })

from django.shortcuts import render, redirect
from django import forms
from .models import House
from users.models import CustomUser
from .form import HouseRegisterForm, HouseEditForm
from users.models import CustomUser


# Create your views here.

def house_create_view(request):
    user = CustomUser.objects.get(email=request.user)
    print(request.method)
    if request.method == 'POST':
        print('its post')
        form = HouseRegisterForm(request.POST, request.FILES or None)
        print(form.is_valid())
        print(form.cleaned_data)
        if form.is_valid():
            obj = House(**form.cleaned_data)
            print('\n\nsaving house\n\n')
            obj.save()
            print(House.objects.all())
            print('\n\n')
    if (user is not None):
        if user.is_host:
            return render(request, 'newHouse.html', {'form': HouseRegisterForm()})
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
        else:
            print(form.errors)
            return render(request, 'homeEdit.html', {'form': form})
        return redirect('../../../')
    form = HouseEditForm(instance=instance)
    return render(request, 'homeEdit.html', {'form': form})


def house_detail_view(request, id):
    # house = House.objects.get(id=id)
    # if house is None:
    #     redirect('../../404')
    # else:
    return render(request, 'homeDetails.html', {'house': {
            'name' : folan,
            'owner' : folani,
            'rooms' : 5,
            'beds' : 2,
            'area' : 45,
            'max_cap' : 5,
            'neighbourhood' : 22,
            'price_per_night' : 65,
        }})


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

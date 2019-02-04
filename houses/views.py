from django.shortcuts import render, redirect
from django import forms
from .models import House
from users.models import CustomUser
from .form import HouseRegisterForm, HouseEditForm


# Create your views here.

def house_create_view(request):
    user = CustomUser.objects.get(email=request.user)
    if request.method == 'POST':
        form = HouseRegisterForm(request.POST)
        if form.is_valid():
            obj = House(**form.cleaned_data)
            obj.save()
    if (user is not None):
        if user.is_host:
            return render(request, 'newHouse.html', {'form': HouseRegisterForm()})
    return redirect('../../users/login')


def house_edit_view(request, id):
    instance = House.objects.get(id=id)
    form = HouseEditForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('../../../')
    return render(request, 'homeEdit.html', {'form': form})

def house_detail_view(request, id):
    house = House.objects.get(id = id)
    if house is None:
        redirect('../../404')
    else:
        return render(request, 'homeDetails.html', {'house':house})

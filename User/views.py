import json

from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from .forms import LoginForm, RegistrationForm
from django.contrib.auth import authenticate, login, get_user
from django.contrib import messages


def index(request):
    objects = User.objects.filter(is_doctor=True).all()
    context = {
        'doctors': objects,
        'user': request.user
    }
    return render(request=request, template_name='index.html', context=context)


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'register.html', context)


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def doctors_view(request):
    page = request.GET.get('d', 5)
    doctors = User.objects.filter(is_doctor=True).all()
    subDoctors = doctors[:int(page)]
    context = {'length': len(doctors), 'doctors': list(subDoctors.values())}
    return render(request, 'doctors.html', context)


def edit_doctor_view(request, doctor_id):
    doctor = get_object_or_404(User, id=doctor_id)
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('doctors')
        context = {'form': form, 'doctors': doctor}
    else:
        if doctor_id:
            form = RegistrationForm(initial={
                'name': doctor.name, 'email': doctor.email, 'password1': doctor.password, 'password2': doctor.password, 'image': doctor.image, 'specialty': doctor.specialty, 'is_superuser': doctor.is_superuser, 'is_doctor': doctor.is_doctor,
            })
        else:
            form = RegistrationForm
        context = {'form': form}
    return render(request, 'register.html', context)


def delete_doctor_view(request, doctor_id):
    product = get_object_or_404(User, id=doctor_id)
    product.delete()
    return redirect('doctors')

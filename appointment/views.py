from django.shortcuts import render, get_object_or_404, redirect, reverse
from User.models import User
from .forms import AppointmentForm, CompleteAppointmentForm
from django.contrib.auth import get_user
from .models import Appointment


def appointments_view(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
        redirect('home')
    else:
        doctor_id = request.GET.get('doctor_id')
        if doctor_id:
            doctor = User.objects.get(id=doctor_id)
            form = AppointmentForm(initial={'doctor': doctor})
        else:
            form = AppointmentForm()
    return render(request, 'appointments.html', {'form': form})


def profile_view(request):
    user = get_user(request=request)
    is_done = request.GET.get('done')
    is_done = 0 if not is_done else is_done
    if user.is_superuser:
        appointments = Appointment.objects.filter(is_done=is_done).all()
    else:
        appointments = Appointment.objects.filter(doctor_id=user.id, is_done=is_done).all()
    is_done = True if is_done == '1' else False
    context = {
        'is_done': is_done,
        'appointments': appointments,
    }
    return render(request, 'profile.html', context)


def complete_appointment_view(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    if request.method == 'POST':
        form = CompleteAppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.instance.is_done = True
            form.save()
            return redirect(reverse('profile')+'?done=0')
    else:
        form = CompleteAppointmentForm(instance=appointment)
    return render(request, 'complete_appointment.html', {'form': form})


def note_view(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    context = {
        'appointment': appointment
    }
    return render(request, 'note.html', context)

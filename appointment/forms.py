from django import forms
from django.forms import widgets
from User.models import User
from .models import Appointment
from django.db import models


class AppointmentForm(forms.ModelForm):
    doctor = forms.ModelChoiceField(
        queryset=User.objects.filter(is_doctor=True).all(),
        empty_label='الطبيب المختص',
        widget=forms.Select(attrs={'class': 'choice-field'}),
        initial=None
    )

    class Meta:
        model = Appointment
        fields = ['name', 'phone', 'doctor', 'age', 'gender', 'datetime']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'text-field', 'placeholder': 'الاسم الثلاثي'}),
            'phone': widgets.TextInput(attrs={'class': 'text-field', 'placeholder': 'رقم الهاتف'}),
            'age': widgets.NumberInput(attrs={'class': 'num-field', 'placeholder': 'العمر'}),
            'gender': widgets.TextInput(attrs={'class': 'text-field', 'placeholder': 'الجنس'}),
            'datetime': widgets.DateTimeInput(attrs={'class': 'datetime-field', 'placeholder': 'موعد الحجز (تاريخاًُ ووقتاً)'})
        }


class CompleteAppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = ['note']
        widgets = {
            'note': widgets.Textarea(attrs={'class': 'text-field', 'placeholder': 'الملاحظة'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initial['is_done'] = True

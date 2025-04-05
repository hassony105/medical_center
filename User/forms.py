from django import forms
from django.forms import widgets
from django.contrib.auth.forms import UserCreationForm
from .models import User


class RegistrationForm(UserCreationForm):
    name = forms.CharField(widget=widgets.TextInput(attrs={'class': 'text-field', 'placeholder': 'الاسم الكامل'}))
    email = forms.EmailField(widget=widgets.EmailInput(attrs={'class': 'text-field', 'placeholder': 'الايميل'}))
    password1 = forms.CharField(widget=widgets.PasswordInput(attrs={'class': 'text-field', 'placeholder': 'الرمز'}))
    password2 = forms.CharField(widget=widgets.PasswordInput(attrs={'class': 'text-field', 'placeholder': 'تأكيد الرمز'}))
    image = forms.ImageField(widget=widgets.FileInput(attrs={'class': 'file-field', 'accept': 'image/*'}), required=True)
    specialty = forms.CharField(widget=widgets.TextInput(attrs={'class': 'text-field', 'placeholder': 'التخصص'}), required=True)
    is_superuser = forms.BooleanField(widget=widgets.CheckboxInput(attrs={'class': 'check-field'}), required=False)
    is_doctor = forms.BooleanField(widget=widgets.CheckboxInput(attrs={'class': 'check-field'}), required=False)

    class Meta:
        model = User
        fields = ('name', 'email', 'password1', 'password2', 'image', 'specialty', 'is_superuser', 'is_doctor')
        error_messages = 'Error'


class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'text-field', 'placeholder': 'الايميل'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'text-field', 'placeholder': 'الرمز'}))

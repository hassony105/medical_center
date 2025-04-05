"""
URL configuration for medical_center project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from User.views import index, login_view, register_view, doctors_view, edit_doctor_view, delete_doctor_view
from appointment.views import appointments_view, profile_view, complete_appointment_view, note_view


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('doctors/', doctors_view, name='doctors'),
    path('appointments/', appointments_view, name='appointments'),
    path('done/<int:appointment_id>', complete_appointment_view, name='done'),
    path('note/<int:appointment_id>', note_view, name='note'),
    path('about/', index, name='about'),
    path('login/', login_view, name='login'),
    path('signup/', register_view, name='signup'),
    path('edit/<int:doctor_id>', edit_doctor_view, name='edit'),
    path('delete/<int:doctor_id>', delete_doctor_view, name='delete'),
    path('profile/', profile_view, name='profile'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

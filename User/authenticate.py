from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from .models import Doctor


class CustomAuth(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        UserModel = get_user_model()

        try:
            # Try to authenticate against the User model
            user = UserModel.objects.get(email=email)
            if user.check_password(password):
                return user

        except UserModel.DoesNotExist:
            pass

        try:
            # Try to authenticate against the Doctor model
            doctor = Doctor.objects.get(email=email)
            if doctor.password == password:
                return doctor

        except Doctor.DoesNotExist:
            pass

    def get_user(self, user_id):
        try:
            return Doctor.objects.get(pk=user_id)
        except Doctor.DoesNotExist:
            return None

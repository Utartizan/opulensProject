from django.contrib.auth.backends import ModelBackend # type: ignore
from django.contrib.auth import get_user_model # type: ignore

class EmailOrUsernameModelBackend(ModelBackend):
    """
    Custom authentication backend that allows users to log in using either their username or email.
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        
        # Try to get the user using either username or email
        try:
            user = UserModel.objects.get(username=username)
        except UserModel.DoesNotExist:
            try:
                user = UserModel.objects.get(email=username)
            except UserModel.DoesNotExist:
                return None

        # If we found the user, check the password
        if user.check_password(password):
            return user
        return None

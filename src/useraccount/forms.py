from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from useraccount.models import Profile
from betterforms.multiform import MultiModelForm


User = get_user_model()


class UserSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "username",
            "password1",
            "password2",
            "address",
            "contact",
        )


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "username",
            "address",
            "contact",
        )


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            "profile_picture",
            "location",
            "about",
        )

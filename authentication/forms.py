from django import forms
from django.contrib.auth import get_user_model
from core.models import Profile

User = get_user_model()


# Authentication forms
class LoginForm(forms.Form):
    class Meta:
        model = Profile

        username = forms.CharField(max_length=30)
        password = forms.CharField(
            widget=forms.PasswordInput(
                attrs={
                    "class": "form-control",
                    "id": "user_password"
                }
            )
        )

        def clean_username(self):
            username = self.cleaned_data.get("username")
            user_qs = User.objects.filter(username__iexact=username)

            if not user_qs.exists:
                raise forms.ValidationError("This is an invalid user.")
                return username


class SignOutForm(forms.Form):
    class Meta:
        model: Profile

        username = forms.CharField(max_length=30)
        email = forms.EmailField(required=True)
        password1 = forms.CharField(
            widget=forms.PasswordInput(
                attrs={
                    "class": "form-control",
                    "id": "user_password"
                }
            )
        )
        password2 = forms.CharField(
            widget=forms.PasswordInput(
                attrs={
                    "class": "form-control",
                    "id": "user_password"
                }
            )
        )

        def clean_username(self):
            username = self.cleaned_data.get("username")
            user_qs = User.objects.filter(username__iexact=username)

            if user_qs.exists:
                raise forms.ValidationError("This username is already taken.")
                return username

        def clean_email(self):
            email = self.cleaned_data.get("email")
            user_qs = User.objects.filter(email__iexact=email)

            if user_qs.exists:
                raise forms.ValidationError("This email has a registered account")
                return username

from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


# Authentication forms
class LoginForm(forms.Form):
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

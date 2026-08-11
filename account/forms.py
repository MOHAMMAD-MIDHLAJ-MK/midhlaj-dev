from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


# =========================================================
# LOGIN FORM
# =========================================================

class LoginForm(AuthenticationForm):

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "account-input",
                "placeholder": "Enter username",
                "autocomplete": "username",
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "account-input",
                "placeholder": "Enter password",
                "autocomplete": "current-password",
            }
        )
    )


# =========================================================
# REGISTER FORM
# =========================================================

class RegisterForm(forms.ModelForm):

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "account-input",
                "placeholder": "Create password",
                "autocomplete": "new-password",
            }
        )
    )

    confirm_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "account-input",
                "placeholder": "Confirm password",
                "autocomplete": "new-password",
            }
        )
    )

    class Meta:

        model = User

        fields = [
            "username",
            "email",
        ]

        widgets = {

            "username": forms.TextInput(
                attrs={
                    "class": "account-input",
                    "placeholder": "Choose a username",
                    "autocomplete": "username",
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "class": "account-input",
                    "placeholder": "Enter your email",
                    "autocomplete": "email",
                }
            ),
        }


    # =====================================================
    # PASSWORD VALIDATION
    # =====================================================

    def clean(self):

        cleaned_data = super().clean()

        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password:

            if password != confirm_password:

                raise forms.ValidationError(
                    "Passwords do not match."
                )

        return cleaned_data


    # =====================================================
    # SAVE USER
    # =====================================================

    def save(self, commit=True):

        user = super().save(commit=False)

        user.set_password(
            self.cleaned_data["password"]
        )

        if commit:
            user.save()

        return user
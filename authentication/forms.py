from django import forms
from .models import Users
from django.contrib.auth.forms import UserCreationForm

DOMAIN_CHOICE = [
    ('gmail.com','gmail.com'),
]

class RegisterForm(UserCreationForm):
    email = forms.CharField(error_messages=
        {'required':'Email is required'},
        widget = forms.TextInput(
            attrs={
                'placeholder':"Enter User",
                'class':'form-control',
                'title':"User",
                'id':'email'
            }
        )
    )
    email_domain = forms.ChoiceField(error_messages=
        {'required':'Email Domain is required'},
        choices = DOMAIN_CHOICE,
        widget = forms.Select(
            attrs={
                'class':'form-select',
                'title':"Domain"
            }
        )
    )

    cell_number = forms.CharField(error_messages=
        {'required':'Mobile is required'},
        widget = forms.TextInput(
            attrs={
                'placeholder':"98977XXXXX",
                'class':'form-control',
                'title':"Mobile"
            }
        )
    )
    password = forms.CharField(error_messages=
        {'required':'Password is required'},
        widget = forms.PasswordInput(
            attrs={
                'placeholder':"Enter Password",
                'class':'form-control',
                'title':"Password"
            }
        )
    )
    confirm_password = forms.CharField(error_messages=
        {'required':'Password is required'},
        widget = forms.PasswordInput(
            attrs={
                'placeholder':"Enter Password",
                'class':'form-control',
                'title':"Password"
            }
        )
    )


    class Meta:
        model = Users
        fields = []

        
    
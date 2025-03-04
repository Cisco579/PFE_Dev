from django import forms
from allauth.account.forms import LoginForm
from django.contrib.auth import authenticate

# Include of model user's role management
from .models import CustomUser

class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.fields['login'].widget = forms.TextInput(attrs={'placeholder': 'Email or Username', 'class': 'form-control'})
        self.fields['password'].widget = forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'})
        self.fields['remember'].widget = forms.CheckboxInput(attrs={'class': 'form-check-input'})

    def clean(self):
        cleaned_data = super(CustomLoginForm, self).clean()
        login = cleaned_data.get('login')
        password = cleaned_data.get('password')

        if login and password:
            user = authenticate(username=login, password=password)
            if user is not None:
                if not user.is_active:
                    raise forms.ValidationError("This account is inactive.")
                # Example of role-based validation
                if user.role not in ['admin', 'student', 'visitor']:
                    raise forms.ValidationError("Invalid user role.")
            else:
                raise forms.ValidationError("Invalid login credentials.")
        return cleaned_data
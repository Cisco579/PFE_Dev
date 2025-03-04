from django import forms
from allauth.account.forms import LoginForm, SignupForm
from django.contrib.auth import authenticate
from .models import CustomUser

class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.fields['login'].widget = forms.TextInput(attrs={'placeholder': 'Email or Username', 'class': 'form-control'})
        self.fields['password'].widget = forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'})
        self.fields['remember'].widget = forms.CheckboxInput(attrs={'class': 'form-check-input'})

    def clean(self):
        cleaned_data = super(CustomLoginForm, self).clean()
        if cleaned_data is None:
            return cleaned_data

        login = cleaned_data.get('login')
        password = cleaned_data.get('password')

        if login and password:
            user = authenticate(username=login, password=password)
            if user is not None:
                if not user.is_active:
                    raise forms.ValidationError("This account is inactive.")
                if user.role not in ['admin', 'student', 'visitor']:
                    raise forms.ValidationError("Invalid user role.")
            else:
                raise forms.ValidationError("Invalid login credentials.")
        return cleaned_data

# End of CustomLoginForm

# Start of CustomSignupForm

class CustomSignupForm(SignupForm):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('student', 'Student'),
        ('visitor', 'Visitor'),
    )

    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'})
        self.fields['email'].widget = forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'})
        self.fields['role'] = forms.ChoiceField(choices=self.ROLE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
        self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': 'Confirm password', 'class': 'form-control'})

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.role = self.cleaned_data['role']
        user.save()
        return user

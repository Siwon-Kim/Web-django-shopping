from django import forms
from django.contrib.auth.hashers import check_password
from .models import User

class RegisterForm(forms.Form):
    email = forms.EmailField(
        error_messages={
            'required': 'Please enter your email address'
        },
        max_length=64, label='email'
    )

    password = forms.CharField(
        error_messages={
            'required': 'Please enter your password'
        },
        widget=forms.PasswordInput, label='password'
    )

    re_password = forms.CharField(
        error_messages={
            'required': 'Please re-enter your password'
        },
        widget=forms.PasswordInput, label='confirm password'
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')

        if password and re_password:
            if password != re_password:
                self.add_error('password', 'Passwords do not match!')
                self.add_error('re_password', 'Passwords do not match!')

class LoginForm(forms.Form):
    email = forms.EmailField(
        error_messages={
            'required': 'Please enter your email address'
        },
        max_length=64, label='email'
    )

    password = forms.CharField(
        error_messages={
            'required': 'Please enter your password'
        },
        widget=forms.PasswordInput, label='password'
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            try: 
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                self.add_error('email', 'No email registered')
                return

            if not check_password(password, user.password):
                self.add_error('password', 'Wrong password')
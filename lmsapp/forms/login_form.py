from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django import forms
from django.forms import ValidationError

class LoginForm(AuthenticationForm):
    username = forms.EmailField(max_length=25, required=True, label="Email address")
    
    def clean(self):
        email=self.cleaned_data['username']
        password=self.cleaned_data['password']
        user=None
        try:
            user= User.objects.get(email=email)
            result = authenticate(username=user.username, password=password)

            if(result is not None):
                return result
            else:
                raise ValidationError("Invalid email or password!")
        except:
            raise ValidationError("Invalid email or password!")



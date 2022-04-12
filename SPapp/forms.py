from django import forms
from SPapp.models import Login, Register_details
from django.contrib.auth.forms import UserCreationForm


class login_register(UserCreationForm):
    username = forms.CharField(label='username')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput)

    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2')

class studentregisterform(forms.ModelForm):
    class Meta:
        model = Register_details
        exclude = ('user',)

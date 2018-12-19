from django import forms
from django.contrib.auth.models import User
from .models import UerProfile

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label="密码：",widget=forms.PasswordInput)
    password2 = forms.CharField(label="确认密码：",widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username","email")

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password']!=cd['password2']:
            raise forms.validationError("两次密码不一样")
        return  cd['password2']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UerProfile
        fields=("phone","birth")
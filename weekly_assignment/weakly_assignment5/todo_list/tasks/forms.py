from django import forms
from .models import domain, UserProfileInfo, Task
from django.contrib.auth.models import User

class DomainForm(forms.ModelForm):
    class Meta:
        model = domain
        fields = '__all__'

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('first_name','last_name','domain')

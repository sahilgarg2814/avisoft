from django import forms
from tasks.models import UserProfileInfo,task,domain

class DomainForm(forms.ModelForm):
    class Meta:
        model=domain
        fields='__all__'

class Userform(forms.ModelForm):
    class Meta:
        model=UserProfileInfo
        fields='__all__'

class taskform(forms.ModelForm):
    class Meta:
        model=task
        fields='__all__'
from django import forms
from app1.models import Students_model

class student_form(forms.ModelForm):
    class Meta:
        model=Students_model
        fields=[
            "student_Name",
            "student_Roll",
            "student_domain"
        ]
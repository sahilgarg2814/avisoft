from django import forms
from app1.models import Students_model

# for taking the data from the user , we use forms
class student_form(forms.ModelForm):
    class Meta:
        model=Students_model
        fields=[
            "student_Name",
            "student_Roll",
            "student_domain"
        ]
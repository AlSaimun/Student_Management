from django import forms
from . models import Student

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['id','name','email','phone_number','year','blood_grp']
        labels ={'phone_number':'Phone no','blood_grp':'Blood group'}

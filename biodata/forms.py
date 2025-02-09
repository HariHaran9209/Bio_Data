from django import forms
from .models import *

# Your Forms Here
class StudentForm(forms.ModelForm):
    class Meta:
        model = studentdata
        fields = ['name', 'age', 'admission_number', 'grade', 'phone_number', 'dob', 'emailid','stream', 'mother_name', 'father_name', 'aadhar_number', 'address', 'pincode', 'alt_phone_number', 'blood_group', 'height', 'weight', 'student_photo']

class TeacherForm(forms.ModelForm):
    class Meta:
        model = teacherdata
        fields = ['teachername', 'email']

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Your Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, label='Your Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}), required=True, label='Your Message')

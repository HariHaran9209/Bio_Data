from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = UserData
        fields = ['username', 'email', 'password1', 'password2', 'role']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].label = "Email Address"
        self.fields['username'].label = "Username"
        self.fields['username'].widget.attrs.update({'placeholder': 'Enter your username'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Enter your email'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Enter your password'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm your password'})
        self.fields['username'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

class BioDataForm(forms.ModelForm):
    class Meta:
        model = BioData
        fields = ['age', 'grade', 'address', 'contact']

class IndexForm(forms.ModelForm):
    class Meta:
        model = Index
        fields = ['studentname', 'dob', 'mothername', 'fathername', 'guardianname', 'aadharno', 'nameinaadhar', 'admissindate', 'address', 'pincode', 'phonenumber', 'alternatenumber', 'emailid', 'BPL', 'AAY', 'EWS', 'CWSN', 'impairment', 'CWSN1', 'disabilityparc', 'nationality', 'oosc', 'mainstream', 'bloodgroup', 'admissionno', 'dateInput', 'stream', 'subjects', 'status', 'grade', 'result', 'marks', 'attendence', 'SLD', 'ASD', 'ADHD', 'special', 'sports', 'scouts', 'internet', 'height', 'weight', 'distance', 'quilification']

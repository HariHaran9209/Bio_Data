from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from openpyxl import Workbook
from .models import *
from .forms import *


# Create your views here.
def fill(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save(commit=False)
            student.student_photo = request.FILES.get('student_photo')
            student.save()
            return redirect('success')
        else:
            print(form.errors)
            messages.error(request, 'Invalid Form')
            return redirect('fill')
    else:
        form = StudentForm()
    return render(request, 'fill.html', {'form': form})

def home(request):
    return render(request, 'home.html')

def success(request):
    return render(request, 'success.html')

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        secret_code = request.POST.get('secret_code')
        if form.is_valid() and secret_code == 'admin':
            user = form.save()  # Create the user
            # Create a UserProfile instance
            teacherdata.objects.create(user=user)
            login(request, user)  # Log the user in
            return redirect('home')  # Redirect to home page
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # Log the user in
            return redirect('home')  # Redirect to home page
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    
    return render(request, 'login.html')

def dashboard(request):
    datas = studentdata.objects.all()
    return render(request, 'dashboard.html', {'datas': datas})

def logout_user(request):
    logout(request)
    return redirect('home')

def details(request, slug):
    data = get_object_or_404(studentdata, slug=slug)
    return render(request, 'details.html', {'data': data})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the data in form.cleaned_data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Send an email (you can customize this part)
            send_mail(
                f'Contact Form Submission from {name}',
                message,
                email,
                [settings.DEFAULT_FROM_EMAIL],  # Set this in your settings.py
                fail_silently=False,
            )

            return render(request, 'success.html')  # Redirect to a success page
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

def export(request):
    # Create a workbook and add a worksheet
    workbook = Workbook()
    worksheet = workbook.active
    worksheet.title = 'Student Data'

    # Define your headers
    headers = ['Name', 'Age', 'Admission Number', 'Grade', 'Phone Number', 'Date Of Birth', 'Email Id', 'Stream', 'Mother Name', 'Father Name', 'Aadhar Number', 'Address', 'Pincode', 'Alternate Phone Number', 'Blood Group', 'Height', 'Weight']  # Replace with your actual column names
    worksheet.append(headers)

    # Fetch data from your model
    data = studentdata.objects.all().values_list('name', 'age', 'admission_number', 'grade', 'phone_number', 'dob', 'emailid', 'stream', 'mother_name', 'father_name', 'aadhar_number', 'address', 'pincode', 'alt_phone_number', 'blood_group', 'height', 'weight')  # Replace with your actual fields

    # Write data to the worksheet
    for row in data:
        worksheet.append(row)

    # Create an HTTP response with the Excel file
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=data_export.xlsx'
    workbook.save(response)
    return response

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)

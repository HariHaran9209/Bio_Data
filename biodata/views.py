from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.http import HttpResponseForbidden
from .models import *
from django.http import HttpResponse
from .forms import *

# Create your views here.
def hello(request):
    return render(request, 'landing.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            # Check if the user is registering as an admin
            if 'role' in request.POST and request.POST['role'] == 'admin':
                user.is_staff = True  # Mark the user as staff
                user.is_superuser = True
                user.save()
            
            login(request, user)
            messages.success(request, 'Registration successful! You are now logged in.')
            return redirect('home')
        else:
            messages.error(request, 'Registration failed. Please check the form for errors.')
    else:
        form = UserRegistrationForm()
    return render(request, './register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:  # Redirect logged-in users
        messages.info(request, 'You are already logged in.')
        return redirect('home')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Login successful! Welcome back.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    return render(request, 'home.html', {'user': request.user})

@login_required
def submit_biodata(request):
    if hasattr(request.user, 'biodata'):
        return redirect('view_biodata')

    if request.method == 'POST':
        form = BioDataForm(request.POST)
        if form.is_valid():
            biodata = form.save(commit=False)
            biodata.user = request.user
            biodata.save()
            return redirect('view_biodata')
    else:
        form = BioDataForm()
    return render(request, 'submit_biodata.html', {'form': form})

@login_required
def admin_dashboard(request):
    if not request.user.is_staff:
        return HttpResponseForbidden("You do not have permission to access this page.")

    biodata_list = BioData.objects.all()
    return render(request, 'admin_dashboard.html', {'biodata_list': biodata_list})

@login_required
def view_biodata(request):
    # Ensure the user can only view their own bio-data
    biodata = get_object_or_404(BioData, user=request.user)
    return render(request, 'view_biodata.html', {'biodata': biodata})

@login_required
def edit_biodata(request):
    # Ensure the user has bio-data to edit
    if not hasattr(request.user, 'biodata'):
        return redirect('submit_biodata')

    biodata = request.user.biodata
    if request.method == 'POST':
        form = BioDataForm(request.POST, instance=biodata)
        if form.is_valid():
            form.save()
            return redirect('view_biodata')
    else:
        form = BioDataForm(instance=biodata)
    return render(request, 'edit_biodata.html', {'form': form})

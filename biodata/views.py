from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.core.management import call_command
from django.http import HttpResponseForbidden
from django.http import HttpResponse
from django.db import connection
from .models import *
from .forms import *
import io

# Create your views here.    
def custom_404(request, exception):
    return render(request, '404.html', status=404)

def register(request):
    if request.user.is_authenticated:
        messages.info(request, 'You are already logged in.')
        return redirect('home')
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        secret_code = request.POST.get('secret_code')
        if form.is_valid():
            user = form.save()

            # Check if the user entered the secret code for admin registration
            if 'role' in request.POST and request.POST['role'] == 'admin':
                if secret_code == 'adminonly':  # Replace with your secret code
                    user.is_staff = True  # Mark the user as staff
                    user.is_superuser = True
                    user.save()
                    messages.success(request, 'Admin account created successfully!')
                else:
                    messages.error(request, 'Invalid secret code. Cannot create an admin account.')
                    user.delete()  # Remove the user record if secret code is invalid
                    return redirect('register')
            else:
                messages.success(request, 'Student account created successfully!')

            login(request, user)
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
    if not request.user.is_authenticated:
        return redirect('login')
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


@login_required
def editindex(request):
    # Ensure the user has bio-data to edit
    if not hasattr(request.user, 'index'):
        return redirect('index')

    index = request.user.index
    if request.method == 'POST':
        form = IndexForm(request.POST, instance=index)
        if form.is_valid():
            form.save()
            return redirect('showindex')
    else:
        form = IndexForm(instance=index)
    return render(request, 'editindex.html', {'form': form})

@login_required
def showindex(request):
    index = get_object_or_404(Index, user=request.user)
    return render(request, 'showindex.html', {'index': index})

@login_required
def admin_data(request):
    if not request.user.is_staff:
        return HttpResponseForbidden("You do not have permission to access this page.")

    index_list = Index.objects.all()
    return render(request, 'admin-data.html', {'index_list': index_list})

@login_required
def index(request):
    if hasattr(request.user, 'index'):
        return redirect('showindex')

    if request.method == 'POST':
        form = IndexForm(request.POST)
        if form.is_valid():
            biodata = form.save(commit=False)  # Save form but don’t commit to database
            biodata.user = request.user        # Associate with the logged-in user
            biodata.save()                     # Now save to the database
            return redirect('showindex')         # Redirect to a success page
    else:
        form = IndexForm()
    return render(request, 'index.html', {'form': form})

def run_migrations(request):
    try:
        call_command('migrate')
        return HttpResponse("Migrations applied successfully!")
    except Exception as e:
        return HttpResponse(f"Error: {e}")

def show_migrations(request):
    out = io.StringIO()
    call_command('showmigrations', stdout=out)
    return HttpResponse(f"<pre>{out.getvalue()}</pre>")

def check_table(request):
    with connection.cursor() as cursor:
        cursor.execute("""
        SELECT table_name FROM information_schema.tables
        WHERE table_name='biodata_index';
        """)
        exists = cursor.fetchone()
    return HttpResponse(f"Table exists: {exists}")

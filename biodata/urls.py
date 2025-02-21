from django.urls import path
from .views import *

urlpatterns = [
    path('fill/', fill, name='fill'),
    path('home/', home, name='home'),
    path('success/', success, name='success'),
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('contact/', contact, name='contact'),
    path('farewell/', farewell, name='farewell'),
    path('export/', export, name='export'),
    path('dashboard/', dashboard, name='dashboard'),
    path('dashboard/details/<slug:slug>', details, name='details'),
    path('testing/', testing, name='testing'),
    path('portfolio/', portfolio, name='portfolio'),
]

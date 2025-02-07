from django.urls import path
from django.conf.urls import handler404
from .views import *

urlpatterns = [
    path('fill/', fill, name='fill'),
    path('home/', home, name='home'),
    path('success/', success, name='success'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('contact/', contact, name='contact'),
    path('export/', export, name='export'),
    path('dashboard/', dashboard, name='dashboard'),
    path('dashboard/details/<slug:slug>', details, name='details'),
]

handler404 = custom_404_view

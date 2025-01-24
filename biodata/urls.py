from django.urls import path
from django.conf.urls import handler404
from .views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('home/', home, name='home'),
    path('submit-biodata/', submit_biodata, name='submit_biodata'),
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('view-biodata/', view_biodata, name='view_biodata'),
    path('edit-biodata/', edit_biodata, name='edit_biodata'),
    path('index/', index, name='index'),
    path('showindex/', showindex, name='showindex'),
    path('editindex/', editindex, name='editindex'),
    path('admin-data/', admin_data, name='admin_data'),
    path('run-migrations/', run_migrations, name='run-migrations'),
]
handler404 = custom_404

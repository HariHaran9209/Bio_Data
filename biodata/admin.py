from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

class UserDataAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_superuser', 'role')

# Register your models here.
admin.site.register(BioData)
admin.site.register(UserData, UserDataAdmin)
admin.site.register(Index)

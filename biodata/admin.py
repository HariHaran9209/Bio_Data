from django.contrib import admin
from .models import *

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'grade', 'dob', 'stream', 'admission_number')
    prepopulated_fields = {"slug": ("name", "admission_number")}

admin.site.register(studentdata, StudentAdmin)

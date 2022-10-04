from atexit import register
from django.contrib import admin
from .models import User
# Register your models here.

@admin.register(User)
class AdminRegister(admin.ModelAdmin):
    list_display = ['student_name','teacher_name','email','password']
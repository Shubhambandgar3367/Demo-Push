from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'email', 'section', 'address')

# Register your models here.

admin.site.register(Student, StudentAdmin)
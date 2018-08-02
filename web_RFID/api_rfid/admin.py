from django.contrib import admin
from .models import Student

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'carear', 'status')
    search_fields = ('name', 'code', 'status')
    

admin.site.register(Student, StudentAdmin)

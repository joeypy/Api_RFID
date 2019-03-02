from django.contrib import admin
from .models import Student

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    readonly_fields = ['student_id', 'created']
    list_display = [ 'name', 'last_name', 'cedula', 'card_code', 'career', 'status', 'solvency_status']
    #search_fields = ['name', 'last_name', 'code', 'status']
    

admin.site.register(Student, StudentAdmin)

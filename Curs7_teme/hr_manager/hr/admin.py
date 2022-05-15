from django.contrib import admin
from .models import Employer, Employee

@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    pass

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass
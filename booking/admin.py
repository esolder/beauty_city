from django.contrib import admin

from .models import Category, Service, Specialty, Employee, Appointment, Review

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price']


@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    ...


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    ...


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'service', 'date', 'time', 'employee']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    ...
from django.contrib import admin

from taxi.models import Driver, Manufacturer, Car

# Register your models here.
admin.site.register(Manufacturer)
@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Additional info", {"fields": ("license_number",)}),
    )
    add_fieldsets = (
        ("Additional info", {"fields": ("license_number",)}),
    )

    list_display = ("username", "email", "first_name", "last_name", "license_number")

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    search_fields = ("model", "manufacturer")

from django.contrib import admin

from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "requested_date", "status", "created_at")
    list_filter = ("status", "requested_date")
    search_fields = ("name", "email", "notes")
    readonly_fields = ("created_at",)

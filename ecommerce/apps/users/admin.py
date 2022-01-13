from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "email", "name", "last_name"]
    list_display_links = ["username", "email"]
    search_fields = ["username", "email", "name", "last_name"]

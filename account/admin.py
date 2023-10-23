from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


# Reference : UserAdmin class [ https://github.com/django/django/blob/main/django/contrib/auth/admin.py ]
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    # Controls which fields are displayed on the change list page of the admin
    list_display = [
        "id",
        "email",
        "name",
        "is_staff",
        "is_superuser",
    ]

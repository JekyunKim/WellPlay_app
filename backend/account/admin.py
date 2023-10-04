from django.contrib import admin
from .models import User, Follow


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user_id",
        "email",
        "is_superuser",
        "is_active",
        "created_at",
        "updated_at",
    )


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ("id", "from_user", "to_user",)

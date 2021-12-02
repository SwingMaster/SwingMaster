from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'user_name',
        'user_id',
        'user_nickname',
        'user_pw',
        'user_email',
        'user_register_dttm'
    )
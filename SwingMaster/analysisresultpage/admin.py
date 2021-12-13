from django.contrib import admin
from .models import UserScore

@admin.register(UserScore)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'userscore_id',
        'userscore_nickname',
        'userscore_score'
    )

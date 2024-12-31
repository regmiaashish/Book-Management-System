from django.contrib import admin

# Register your models here.
from user.models import UserBalance

@admin.register(UserBalance)
class UserbalanceAdmin(admin.ModelAdmin):
    list_display = ['user','balance']
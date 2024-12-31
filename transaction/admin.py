from django.contrib import admin
from transaction.models import Transaction

# Register your models here.
@admin.register(Transaction)
class UserbalanceAdmin(admin.ModelAdmin):
    list_display = ['name','amount']
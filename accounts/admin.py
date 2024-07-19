from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
import accounts.models as accounts 

@admin.register(accounts.CustomUser)
class AdminUser(UserAdmin):
    list_display = ("username", "email")
    search_fields = ('username',)
    fieldsets = (
        ("System", {'fields': ('username', 'password')}), 
        ("Personal Info", {'fields':('last_name','first_name','middle_name','email', 'phone')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions')}), 
        ('Important dates', {'fields': ('last_login', 'date_joined')})
    )
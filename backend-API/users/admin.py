from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Role

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age', 'location', 'description', 'role')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('age', 'location', 'description', 'role')}),
    )
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'role']
    search_fields = ['username', 'email', 'first_name', 'last_name']

class RoleAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Role, RoleAdmin)

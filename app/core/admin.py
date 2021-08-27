from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUSerAdmin
from django.utils.translation import gettext as _
from core import models


class UserAdmin(BaseUSerAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name',)}),
        (
            _('Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
        (_('Imortant dates'), {'fields': ('last_login',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}),
        # comma in the end to let python know its a list not and object
    )


admin.site.register(models.User, UserAdmin)

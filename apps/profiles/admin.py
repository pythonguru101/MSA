from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
from django.utils.translation import ugettext as _

from .models import User


class UserAdmin(BaseUserAdmin):
    inlines = [

    ]
    fieldsets = (
        (None,
         {'fields': ('username', 'email', 'password', 'photo', 'image_tag', 'birthday', 'location', 'creation_time')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    readonly_fields = ('image_tag',)


admin.site.register(User, UserAdmin)

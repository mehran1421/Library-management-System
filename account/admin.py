from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

UserAdmin.fieldsets[2][1]['fields'] = (
										'slug',
										'is_active',
										'is_staff',
										'is_superuser',
										'address',
										'groups',
										'user_permissions'
									)
UserAdmin.list_display += ('slug', 'address')

admin.site.register(User, UserAdmin)

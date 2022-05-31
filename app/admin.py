from django.contrib import admin

from .models import Users, Role, Department, Address

admin.site.register(Users)
admin.site.register(Role)
admin.site.register(Department)
admin.site.register(Address)

from django.contrib import admin
from ipfree.models import Machine

class MachineAdmin(admin.ModelAdmin):
    list_display = ("hostname", "description", "ipaddress")

admin.site.unregister(Machine)
admin.site.register(Machine, MachineAdmin)

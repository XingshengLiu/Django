from django.contrib import admin
from sign.models import Event, Guest


# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'start_time', 'id']


class GuestAdmin(admin.ModelAdmin):
    list_display = ['realName', 'phone', 'email', 'sign', 'create_time', 'event']


admin.site.register(Event, EventAdmin)
admin.site.register(Guest, GuestAdmin)

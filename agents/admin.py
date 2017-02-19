from django.contrib import admin
from .models import Facility, Agent


class FacilityAdmin(admin.ModelAdmin):
    fields = ('name', 'phone_number', 'address', 'public_email', 'accept_appointment_types', 'accept_dental_plans', 'accept_uninsured', 'accept_walkins')
    list_display = ('name', 'phone_number', 'public_email', 'accept_uninsured', 'accept_walkins', 'created', 'modified')

class AgentAdmin(admin.ModelAdmin):
    fields = ('user', 'facility')
    list_display = ('user', 'facility')

admin.site.register(Facility, FacilityAdmin)
admin.site.register(Agent, AgentAdmin)

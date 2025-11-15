from django.contrib import admin
from .models import Events,EventHosts,Hosts,Registration

admin.site.register(Events)
admin.site.register(EventHosts)
admin.site.register(Hosts)
admin.site.register(Registration)


# Register your models here.

from django.contrib import admin

# Register your models here.

from .models import Event,Ticket,User,Payment,Registration,Notification

admin.site.register(Event)
admin.site.register(User)
admin.site.register(Payment)
admin.site.register(Registration)
admin.site.register(Ticket)
admin.site.register(Notification)

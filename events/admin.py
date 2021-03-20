from django.contrib import admin

# Register your models here.
# Venue,
from .models import Event
# admin.site.register(Venue)
#admin.site.register(MyClubUser)
admin.site.register(Event)

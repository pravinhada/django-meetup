from django.contrib import admin
from django.db import models

from .models import Meetup, Location, Participant
# Register your models here.


class MeetupAdmin(admin.ModelAdmin):
    list_display = ("title", "description",)
    list_filter = ("title", "location",)
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Meetup, MeetupAdmin)

admin.site.register(Location)

admin.site.register(Participant)
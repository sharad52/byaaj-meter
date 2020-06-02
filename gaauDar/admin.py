from django.contrib import admin
from .models import Icalc

@admin.register(Icalc)
class IcalcAdmin(admin.ModelAdmin):
    list_display = ('principle',)

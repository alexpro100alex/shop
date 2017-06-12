from django.contrib import admin
from .models import *

class SubscriberAdmin(admin.ModelAdmin):
    search_fields = ["name", "email"]
    list_display = ["name", "email"]
    list_filter = ["email"]

    fields = ["email"]

    class Meta:
        model = Subscriber

admin.site.register(Subscriber, SubscriberAdmin)
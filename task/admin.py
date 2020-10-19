from django.contrib import admin
from . models import Lead, Followup, Lead_fields

# Register your models here.
admin.site.register(Lead)
admin.site.register(Followup)
admin.site.register(Lead_fields)
from django.contrib import admin
from .models import Visit, Master, Service

admin.site.register(Master)
admin.site.register(Service)
admin.site.register(Visit)
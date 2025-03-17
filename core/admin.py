from django.contrib import admin
from .models import Visit, Master, Service, Review

admin.site.register(Master)
admin.site.register(Service)
admin.site.register(Visit)
admin.site.register(Review)
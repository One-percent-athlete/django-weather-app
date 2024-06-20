from django.contrib import admin
from django.contrib.auth.models import Group
from .models import City

# Register your models here.
admin.site.register(City)
admin.site.unregister(Group)
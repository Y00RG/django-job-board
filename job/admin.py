from django.contrib import admin

# Register your models here.

from .models import Job

# add job app to admin panel
admin.site.register(Job)
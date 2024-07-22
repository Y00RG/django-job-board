from django.contrib import admin

# Register your models here.

from .models import Job, Category

# add apps to admin panel
admin.site.register(Job)
admin.site.register(Category)


from django.contrib import admin

# Register your models here.

from .models import Job, Category, Apply

# add apps to admin panel
admin.site.register(Job)
admin.site.register(Category)
admin.site.register(Apply)


from django.contrib import admin

# Register your models here.
from .models import Profile, City

# Register here
admin.site.register(Profile)
admin.site.register(City)
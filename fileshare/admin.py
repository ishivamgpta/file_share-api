from django.contrib import admin
from fileshare import models

# Register your models here.
admin.site.register([
    models.File,
])

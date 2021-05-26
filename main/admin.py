from django.contrib import admin
from .models import Donors
# Register your models here.

class DonorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Donors,DonorAdmin)
from django.contrib import admin
from .models import Portfolio

# Register your models here.

# admin.site.register(Portfolio)

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title','image','created_at')
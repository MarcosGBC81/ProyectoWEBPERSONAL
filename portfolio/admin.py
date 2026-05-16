from django.contrib import admin
from .models import Portfolio, Profile


class PortfolioAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class ProfileAdmin(admin.ModelAdmin):
    pass
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Profile, ProfileAdmin)
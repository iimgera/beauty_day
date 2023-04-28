from django.contrib import admin

from apps.team.models import Team, Gallary


admin.site.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'last_name',
        'photo',
    )



admin.site.register(Gallary)
class GallaryAdmin(admin.ModelAdmin):
    pass


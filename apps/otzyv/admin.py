from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.otzyv.models import (
    Review, 
    Article,
    ArticleImage,
    )


@admin.register(Review)
class UserAdmin(admin.ModelAdmin):
    list_display = (
            'id',
            'name',
            'description',
            'quality',
            'atmosphere',
    )


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass


@admin.register(ArticleImage)
class ArticleImageAdmin(admin.ModelAdmin):
    pass
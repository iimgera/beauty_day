from django.contrib import admin

from apps.discounts.models import (
    Promotion,
    Category,
    Subcategory,
    Service,
)


@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display =  (
            'id', 
            'image', 
            'description'
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
            'id', 
            'name'
    )


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = (
            'id', 
            'name', 
            'category'
    )


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
            'id', 
            'subcategory', 
            'price', 
        )
        


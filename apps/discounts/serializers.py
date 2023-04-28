from rest_framework import serializers

from .models import (
    Promotion,
    Category, 
    Subcategory, 
    Service
)


class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = (
            'id', 
            'image', 
            'description',
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id', 
            'name'
        )


class SubcategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Subcategory
        fields = (
            'id', 
            'name', 
            'category'
        )


class ServiceSerializer(serializers.ModelSerializer):
    subcategory = SubcategorySerializer()

    class Meta:
        model = Service
        fields = (
            'id', 
            'subcategory', 
            'price', 
            
        )



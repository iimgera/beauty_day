from rest_framework import serializers

from apps.otzyv.models import (
    Review,
    Article,
    ArticleImage,
)


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = (
            'id',
            'name',
            'description',
            'quality',
            'atmosphere',
        )


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = (
           'title',
           'sub_title',
           'content',
           'is_publish',
        )
        
    def validate_is_publish(self, value):
        if not value and self.instance:
            # при обновлении объекта, запрещаем снимать флаг публикации
            if self.instance.is_publish:
                raise serializers.ValidationError("Нельзя убрать флаг публикации")
        return value
    

class ArticleImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleImage
        fields = (
            'article',
            'image',
        )
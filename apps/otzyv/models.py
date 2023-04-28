from django.db import models


QUALITY_CHOICES = (
    ("плохое", "плохое"),
    ("среднее", "среднее"),
    ("удовлетворительное", "удовлетворительное"),
    ("хорошее", "хорошее"),
    ("отличное", "отличное"),
)


ATMOSPHERE_CHOICES = (
    ("плохая", "плохая"),
    ("средняя", "средняя"),
    ("удовлетворительная", "удовлетворительная"),
    ("хорошая", "хорошая"),
    ("отличная", "отличная"),
)


class Review(models.Model):
    name = models.CharField(
        max_length=100, 
        blank=False, 
        verbose_name='имя',
    )
    description = models.TextField(
        blank=False, 
        verbose_name='отзыв',
    )
    quality = models.CharField(
        max_length=20, 
        choices = QUALITY_CHOICES , 
        default = "удовлетворительное", 
        verbose_name='качество',
    )
    atmosphere = models.CharField(
        max_length=20, 
        choices = ATMOSPHERE_CHOICES, 
        default = "удовлетворительная", 
        verbose_name='атмосфера',
    )
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отзыв'
<<<<<<< HEAD
        verbose_name_plural = 'Отзывы'
=======
        verbose_name_plural = 'Отзывы'


class Article(models.Model):
    title = models.CharField(
        max_length=255, 
        verbose_name='Название'
    )
    sub_title = models.CharField(
        max_length=255, 
        blank=True, null=True,
        verbose_name='Подзоголовок',
    )
    content = models.TextField(
        verbose_name='Статья'
    )
    is_publish = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'



class ArticleImage(models.Model):
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, 
        related_name='images', 
        verbose_name='Статья'
    )
    image = models.FileField(
        upload_to='Articles/%Y/%m/%d/', 
        verbose_name='Изображения')

    def __str__(self):
        return self.image.name.split('/')[-1]
    
    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
>>>>>>> 3b39b3832f363177dc8b1ce89b1332dd4626bbb4

from django.db import models


class Promotion(models.Model):
    image = models.ImageField(
        verbose_name='Изображения',
        upload_to='promotions/%Y/%m/%d/'
    )
    description = models.TextField(
        verbose_name='Описание'
    )

    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'

    def __str__(self):
        return self.description


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Название категории'
    )
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    name = models.CharField(
        max_length=150, 
        verbose_name='Подкатегория'
    )
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def __str__(self):
        return self.name


class Service(models.Model):
    subcategory = models.ForeignKey(
        Subcategory, 
        on_delete=models.CASCADE,
        verbose_name='Услуга'
    )
    price = models.DecimalField(
        max_digits=6, 
        decimal_places=0,
        verbose_name='Цена'
    )


    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.subcategory


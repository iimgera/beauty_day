from django.db import models


class Team(models.Model):
    name = models.CharField(
        max_length=50, 
        verbose_name='Имя'
    )
    last_name = models.CharField(
        max_length=50, 
        verbose_name='Фамилия'
    )
    photo = models.ImageField(
        upload_to='Team/%Y/%m/%d/'
    )
    position = models.CharField(
        max_length=50, 
        verbose_name='Позиция'
    )

    def __str__(self):
        return f"{self.name} {self.last_name}"
    
    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'


class Gallary(models.Model):
    photo = models.ImageField(
        upload_to='Galary/%Y/%m/%d/'
    )

    def __str__(self):
        return self.photo.name.split('/')[-1]

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галереии'




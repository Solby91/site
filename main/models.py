from django.db import models


class Main(models.Model):

    class Meta():
        verbose_name = 'Главная'
        verbose_name_plural = 'Главная'

    title = models.CharField(max_length=50, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Текст')

    def __str__(self):
        return self.title
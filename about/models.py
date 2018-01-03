from django.db import models


class About(models.Model):

    class Meta():
        verbose_name = 'О компании'
        verbose_name_plural = 'О компании'

    title = models.CharField(max_length=50, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Текст')

    def __str__(self):
        return self.title





from django.db import models


class Contacts(models.Model):

    class Meta():
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'

    title = models.CharField(max_length=50, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Текст')

    def __str__(self):
        return self.title

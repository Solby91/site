from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
import mptt
from django.core.urlresolvers import reverse


class Catalog(MPTTModel):
    class Meta():
        db_table = 'category'
        verbose_name_plural = "Категории"
        verbose_name = "Категория"
        ordering = ('tree_id',)

    name = models.CharField(max_length=50, unique=True, db_index=True, verbose_name="Категория")
    parent = TreeForeignKey('self',blank=True, null=True, related_name='children',db_index=True, verbose_name = u'Родительский класс')
    slug = models.SlugField(max_length=200, unique=True, db_index=True, db_column='slug')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog:GoodsByCategory', args=[self.slug])


    class MPTTMeta:
        level_attr = 'mptt_level'
        order_insertion_by = ['name']


class Goods(models.Model):
    db_table = 'goods_id'
    name = models.CharField(max_length=100,unique=True,verbose_name="Название")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    description = models.TextField(blank=True, verbose_name='Описание')
    vendor_code = models.CharField(max_length=6, unique=True, verbose_name='Артикул')
    category = models.ForeignKey(Catalog, verbose_name='Раздел',related_name='+')
    slug = models.SlugField(max_length=200, unique=True, db_index=True)
    available = models.BooleanField(default=False, verbose_name="В наличии")
    image = models.ImageField(blank=True, verbose_name="Изображение товара")

    class Meta():
        db_table = 'goods' # меняет название таблицы в БД
        verbose_name_plural = "Товары"
        verbose_name = "Товар"
        ordering = ['name']
        index_together = [['id', 'slug']]

    def __str__(self):
        return (self.name)

    def get_absolute_url(self):
        return reverse('catalog:PageWithGood', args=[self.id, self.slug])


mptt.register(Catalog, order_insertion_by = ['name'])




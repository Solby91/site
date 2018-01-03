from django.db import models
from django.core.urlresolvers import reverse


class Catalog(models.Model):
    class Meta():
        db_table = 'category'
        verbose_name_plural = "Категории"
        verbose_name = "Категория"

    name = models.CharField(max_length=50, unique=True, db_index=True, verbose_name="Категория")
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children',db_index=True, verbose_name = u'Родительский класс')
    slug = models.SlugField(max_length=200, unique=True, db_index=True, db_column='slug')
    image = models.ImageField(blank=True, verbose_name="Изображение категории")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog:CategoryList', args=[self.slug])


class Products(models.Model):
    db_table = 'products_id'
    name = models.CharField(max_length=100,unique=True,verbose_name="Название")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    description = models.TextField(blank=True, verbose_name='Описание')
    vendor_code = models.CharField(max_length=6, unique=True, verbose_name='Артикул')
    category = models.ForeignKey(Catalog, verbose_name='Раздел',related_name='+')
    slug = models.SlugField(max_length=200, unique=True, db_index=True)
    available = models.BooleanField(default=False, verbose_name="В наличии")
    image = models.ImageField(blank=True, verbose_name="Изображение товара")

    class Meta():
        db_table = 'products' # меняет название таблицы в БД
        verbose_name_plural = "Товары"
        verbose_name = "Товар"
        ordering = ['name']
        index_together = [['id', 'slug']]

    def get_absolute_url(self):
        cur_obj = self.category_id
        out_obj = Catalog.objects.all()
        for x in out_obj:
            if x.id == cur_obj:
                category_slug = x.slug
        return reverse('catalog:ProductPage', args=[category_slug, self.slug])

    def __str__(self):
        return (self.name)
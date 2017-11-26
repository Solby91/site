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
    name = models.CharField(max_length=50, unique=True, verbose_name="Категория")
    parent = TreeForeignKey('self',blank=True, null=True, related_name='children',db_index=True, verbose_name = u'Родительский класс')
    #url_field = CategoryUrl.url_maker(self)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class MPTTMeta:
        level_attr = 'mptt_level'
        order_insertion_by = ['name']


class Goods(models.Model):
    class Meta():
        db_table = 'goods' # меняет название таблицы в БД
        verbose_name_plural = "Товары"
        verbose_name = "Товар"
        index_together = [['id', 'slug']]

    db_table = 'goods_id'
    name = models.CharField(max_length=100,unique=True,)
    price = models.FloatField(max_length=10)
    description = models.TextField(verbose_name='Description')
    vendor_code = models.CharField(max_length=6, unique=True)  # артикул
    parent = models.ForeignKey(Catalog, blank=True,verbose_name='Раздел',related_name='+')
    slug = models.CharField(max_length=200, unique=True, db_index=True)

    def __str__(self):
        return (self.name + " - ( раздел <" + str(self.parent) + "> )")

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('goods_slug', args=[self.slug])


mptt.register(Catalog, order_insertion_by = ['name'])








"""
# создание текста ссылки в транслите
class CategoryUrl(Catalog):
    category_url = {}
    catalog_obj = Catalog.objects.all()

    def url_maker(self):
        if id.tree_id == 1:
            translit_id = slugify(id)
            CategoryUrl.category_url = {id.name:translit_id}
"""











from haystack import indexes
from .models import Products


class ProductsIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    vendor_code = indexes.CharField(model_attr='vendor_code')
    price = indexes.DecimalField(model_attr='price')

    def get_model(self):
        return Products

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(available=True)

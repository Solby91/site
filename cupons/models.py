from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Cupon(models.Model):
    class Meta():
        verbose_name_plural = "Купоны"
        verbose_name = "Купон"
    code = models.CharField(max_length=50, unique=True, verbose_name="Код")
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    active = models.BooleanField()

    def __str__(self):
        return self.code

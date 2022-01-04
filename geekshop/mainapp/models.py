from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name='название')
    description = models.TextField(blank=True, null=True, verbose_name='описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('-id',)


class Product(models.Model):
    name = models.CharField(max_length=256)
    image = models.ImageField(upload_to='products', blank=True, null=True, verbose_name='картинка')
    short_desc = models.CharField(max_length=256, verbose_name='краткое описание')
    description = models.TextField(blank=True, null=True, verbose_name='описание')
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name='цена')
    quantity = models.PositiveIntegerField(default=0, verbose_name='количество')
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, verbose_name='категория')

    def __str__(self):
        return f'{self.name} | {self.category.name}'

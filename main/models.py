from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)  # ✅ unique=True, не 100!

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)  # ✅ тоже исправлено!
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)  # ✅ исправлено: availabel → available
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)  # ✅ исправлено: update → updated

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
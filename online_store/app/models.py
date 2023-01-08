from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)  # Аргумент db_index, если он равен True, указывает, что это поле должно быть проиндексировано в базе данных, что может повысить производительность запросов к базе данных
    slug = models.SlugField(max_length=200, db_index=True, unique=True)  # This means that you cannot have two records with the same value in that field

    class Meta:
        ordering = ('name',)           # указание порядка
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name                                        # отображение в админке в виде строки


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)              # тип поля(опции поля как аргументы)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='online_store/upload', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)                                                  # дополнительные параметры модели
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name
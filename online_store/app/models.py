from django.conf import settings
from django.db import models




class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    def __str__(self):
        return self.title


class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)              # типа один ко многим, заказ могут делать многие
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)


    def __str__(self):
        return self.user.username































# class Category(models.Model):
#     name = models.CharField(max_length=200, db_index=True)  # Аргумент db_index, если он равен True, указывает, что это поле должно быть проиндексировано в базе данных, что может повысить производительность запросов к базе данных
#     slug = models.SlugField(max_length=200, db_index=True, unique=True)  # This means that you cannot have two records with the same value in that field
#
#     class Meta:
#         ordering = ('name',)           # указание порядка
#         verbose_name = 'Категория'
#         verbose_name_plural = 'Категории'
#
#
#
#
#
# class Product(models.Model):
#     category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)              # тип поля(опции поля как аргументы)
#     name = models.CharField(max_length=200, db_index=True)
#     slug = models.SlugField(max_length=200, db_index=True)
#     image = models.ImageField(upload_to='online_store/upload', blank=True)
#     description = models.TextField(blank=True)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     stock = models.PositiveIntegerField()
#     available = models.BooleanField(default=True)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         ordering = ('name',)                                                  # дополнительные параметры модели
#         index_together = (('id', 'slug'),)
#
#     def __str__(self):
#         return self.name
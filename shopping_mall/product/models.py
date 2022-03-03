from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=256)
    price = models.IntegerField()
    description = models.TextField()
    stock = models.IntegerField()
    register_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'product_list'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
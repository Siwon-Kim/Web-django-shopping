from django.db import models

class Order(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    status = models.CharField(
        choices = (
            ('pending', 'pending'),
            ('refund', 'refund'),
            ('confirmed', 'confirmed'),
            ('delivered', 'delivered'),
        ),
        default='pending', max_length=32
    )
    memo = models.TextField(null=True, blank=True)
    register_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user) + ' ' + str(self.product)

    class Meta:
        db_table = 'order_list'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
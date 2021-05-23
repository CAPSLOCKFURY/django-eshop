from django.db import models


class Order(models.Model):
    DELIVERY_CHOISES = [
        ('', 'other'),
        ('pk', 'pickup'),
        ('dl', 'delivery')
    ]

    user_id = models.CharField(max_length=255)
    order_id = models.CharField(max_length=255)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_type = models.CharField(choices=DELIVERY_CHOISES, max_length=1000)
    comment = models.TextField(max_length=2000, blank=True, null=True)

    def __str__(self):
        return str(self.order_date)

    def get_absolute_url(self):
        return f'/order-details/{self.order_id}'

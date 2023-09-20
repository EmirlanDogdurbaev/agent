from django.db import models
from account.models import User, Producer

MEASUREMENT_TYPE = (
    ("Piece", "Piece"),
    ("Liter", "Liter"),
    ("Kilogram", "Kilogram"),
    ("Meter", "Meter"),
)

DELIVERY_STATUS = (
    ("Delivered", "Delivered"),
    ("In the way", "In the way"),
    ("Preparing for delivery", "Preparing for delivery"),
    ("Searching", "Searching"),
)


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default="")
    quantity = models.IntegerField()
    measure_type = models.CharField(choices=MEASUREMENT_TYPE, max_length=100)
    price = models.IntegerField()
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    produced_date = models.DateTimeField()
    expiration_date = models.DateTimeField()


class Order(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, default="")
    supplier = models.ForeignKey(Producer, on_delete=models.CASCADE, related_name='supplied_orders')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_orders')
    order_date = models.DateTimeField(auto_now_add=True)
    confirm_date = models.DateTimeField(default=None, null=True)
    receiving_date = models.DateTimeField(default=None, null=True)
    delivery_status = models.CharField(choices=DELIVERY_STATUS, max_length=100)

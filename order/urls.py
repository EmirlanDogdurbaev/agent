from .views import *
from django.urls import path

urlpatterns = [
    path('order/create', OrderListCreateAPIView.as_view(), name='order_create'),
    path('order/delete', OrderUpdateDeleteAPIView.as_view(), name='order_delete'),
    path('product/create', OrderListCreateAPIView.as_view(), name='product_create'),
    path('product/delete', OrderUpdateDeleteAPIView.as_view(), name='product_delete'),
]

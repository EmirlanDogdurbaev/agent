from .views import *
from django.urls import path

urlpatterns = [
    path('order/create', OrderListCreateAPIView.as_view(), name='order_create'),
    path('order/delete', OrderUpdateDeleteAPIView.as_view(), name='order_delete'),
]

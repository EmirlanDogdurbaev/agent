from django.shortcuts import render
from rest_framework import permissions, status
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.response import Response
from rest_framework.views import APIView

from account import models as acc_models

from .models import Order, Product
from .serializers import OrderSerializer, ProductSerializer


class OrderListCreateAPIView(ListCreateAPIView):
    # permission to check if user is authenticated
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]


class OrderUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    # permission to check if user is authenticated
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProductListCreateAPIView(ListCreateAPIView):
    # permission to check if user is authenticated
    queryset = Product.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProductUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    # permission to check if user is authenticated
    queryset = Product.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

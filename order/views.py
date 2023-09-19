from django.shortcuts import render
from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from account import models as acc_models
from .models import Order, Product

from .serializers import ProductSerializer, OrderSerializer


class OrderListCreateAPIView(ListCreateAPIView):
    # permission to check if user is authenticated
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # permission_classes = [permissions.IsAuthenticated]


class OrderUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    # permission to check if user is authenticated
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # permission_classes = [permissions.IsAuthenticated]
# class OrderListView(APIView):
#     # add permission to check if user is authenticated
#     permission_classes = [permissions.IsAuthenticated]
#
#         def get(self, request, *args, **kwargs):
#         """
#         List all the device items for given requested user
#         """
#         driver = acc_models.Driver.objects.get(user_id=request.user.id)
#         devices = Device.objects.filter(user=driver.id)
#         serializer = DeviceSerializer(devices, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def post(self, request, *args, **kwargs):
#         """
#         Create the device with given url data
#         """
#         data = request.data
#         driver = acc_models.Driver.objects.get(user_id=request.user.id)
#         data.update({"user": driver.id})
#         serializer = DeviceSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


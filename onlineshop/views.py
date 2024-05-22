from django.shortcuts import render
from .serializers import OrderSerializer
from .models import Order
from rest_framework import generics

# Create your views here.


class ListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class= OrderSerializer



class DetailUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class= OrderSerializer
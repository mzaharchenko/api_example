from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Report, Order, \
    OrderType, OrderStatus
from .serializers import UserSerializer, ReportSerializer, OrderSerializer

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ReportView(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

class OrderView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

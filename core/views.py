from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from . import models
import datetime
import json
from . import serializers
from rest_framework import viewsets

class ColorViewSet(viewsets.ModelViewSet):
    queryset = models.Color.objects.all()
    serializer_class = serializers.ColorSerializer

class SizeViewSet(viewsets.ModelViewSet):
    queryset = models.Size.objects.all()
    serializer_class = serializers.SizeSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer

class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = models.SubCategory.objects.all()
    serializer_class = serializers.SubCategorySerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

class ReviewModelViewSet(viewsets.ModelViewSet):
    queryset = models.ReviewModel.objects.all()
    serializer_class = serializers.ReviewModelSerializers  # Fixed serializer class name


class InventoryView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        inventory = models.InventoryModel.objects.all()
        serializer = serializers.InventoryModelSerializer(inventory, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = serializers.InventoryModel(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class CartView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        customer = request.user.customer
        order, created = models.Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        serializer = serializers.OrderItemSerializer(items, many=True)
        return Response(serializer.data)
    
class CheckoutView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        items = models.OrderItem.objects.all()
        serializer = serializers.OrderItemSerializer(items, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        customer = request.user.customer
        order, created = models.Order.objects.get_or_create(customer=customer, complete=False)
        order.complete = True
        order.transaction_id = datetime.datetime.now().timestamp()
        order.save()
        serializer = serializers.OrderSerializer(order)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class UpdateItemView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        data = json.loads(request.body)
        productId = data['productId']
        action = data['action']
        customer = request.user.customer
        product = models.Product.objects.get(id=productId)
        order, created = models.Order.objects.get_or_create(customer=customer, complete=False)
        orderItem, created = models.OrderItem.objects.get_or_create(order=order, product=product)
        if action == 'add':
            orderItem.quantity += 1
        elif action == 'remove':
            orderItem.quantity -= 1
        orderItem.save()
        if orderItem.quantity <= 0:
            orderItem.delete()

        serializer = serializers.OrderItemSerializer(orderItem)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
class ProcessOrderView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        transaction_id = datetime.datetime.now().timestamp()
        data = json.loads(request.body)
        customer = request.user.customer
        order, created = models.Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id
        if total == order.get_cart_total:
            order.complete = True
        order.save()
        shippingAddress = models.ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            state=data['shipping']['state'],
            zipcode=data['shipping']['zipcode'],
        )
        serializer = serializers.OrderSerializer(order)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

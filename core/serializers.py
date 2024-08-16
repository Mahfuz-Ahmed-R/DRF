from rest_framework import serializers
from .models import Color, Size, Category, SubCategory, Customer, Product, Order, OrderItem, ShippingAddress, InventoryModel, ReviewModel

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(many=False)
    subcategory = serializers.StringRelatedField(many=False)
    class Meta:
        model = Product
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    customer = serializers.StringRelatedField(many=False)
    class Meta:
        model = Order
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    color = serializers.StringRelatedField(many=False)
    size = serializers.StringRelatedField(many=False)
    product = serializers.StringRelatedField(many=False)
    order = serializers.StringRelatedField(many=False)
    class Meta:
        model = OrderItem
        fields = '__all__'

class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = '__all__'

class InventoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryModel
        fields = '__all__'

class ReviewModelSerializers(serializers.ModelSerializer):
    customer = serializers.StringRelatedField(many=False)
    product = serializers.StringRelatedField(many=False)
    class Meta:
        model = ReviewModel
        fields = '__all__'
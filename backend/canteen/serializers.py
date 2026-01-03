from rest_framework import serializers
from .models import MenuItem, OrderItem, Order

# Serializer for MenuItem model
class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'name', 'price']

# Serializer for OrderItem model, with a nested MenuItemSerializer to include menu item details
class OrderItemSerializer(serializers.ModelSerializer):
    menu_item = MenuItemSerializer()  # Nesting MenuItemSerializer to include name and price

    class Meta:
        model = OrderItem
        fields = ['menu_item', 'quantity']

# Serializer for Order model, with a nested OrderItemSerializer to include order items and their menu item details
class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(source='orderitem_set', many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'items', 'status', 'timestamp']

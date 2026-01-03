from rest_framework import viewsets,status
from .models import MenuItem, Order, OrderItem
from rest_framework.response import Response
from .serializers import MenuItemSerializer, OrderSerializer, OrderSerializer

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        items = request.data.get('items', None)

        if not items:
            return Response({'error': 'Missing required field: items'}, status=status.HTTP_400_BAD_REQUEST)

        order = Order.objects.create()

        for item_data in items:
            menu_item_id = item_data.get('id')
            quantity = item_data.get('quantity', 1)

            if not menu_item_id:
                order.delete()
                return Response({'error': 'Invalid item data: missing id'}, status=status.HTTP_400_BAD_REQUEST)

            try:
                menu_item = MenuItem.objects.get(pk=menu_item_id)
            except MenuItem.DoesNotExist:
                order.delete()
                return Response({'error': f'Item with id {menu_item_id} does not exist'}, status=status.HTTP_400_BAD_REQUEST)

            OrderItem.objects.create(order=order, menu_item=menu_item, quantity=quantity)

        serializer = self.get_serializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='menu_images/', null=True, blank=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    ordered_items = models.ManyToManyField('MenuItem', through='OrderItem')  # Use a ManyToManyField through an intermediate model
    status = models.CharField(max_length=50, default='Pending')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.status}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)  # Ensure positive quantity

    def __str__(self):
        return f"Order Item ({self.order.id}): {self.menu_item.name} (x{self.quantity})"
from django.db import models

class Accessory(models.Model):
    CATEGORY_CHOICES = [
        ('Cables', 'Cables'),
        ('Headphones', 'Headphones'),
        ('Charging Docks', 'Charging Docks'),
        ('Gaming Pads', 'Gaming Pads'),
        ('Card Games', 'Card Games'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    stock_quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='accessories/')  # Store images in 'media/accessories/'
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.category})"

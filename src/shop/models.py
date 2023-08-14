from django.db import models
import random

CATEGORIES = [
    ('Cosméticos antiedad', 'Cosméticos antiedad'),
    ('Dieta - Pérdida de peso', 'Dieta - Pérdida de peso'),
    ('Diabetes', 'Diabetes'),
    ('Articulaciones', 'Articulaciones'),
    ('Prostatitis', 'Prostatitis'),
    ('Cistitis', 'Cistitis'),
    ('Aumento', 'Aumento'),
    ('Parásitos', 'Parásitos'),
    ('Hipertensión', 'Hipertensión'),
    ('Cabello', 'Cabello'),
    ('Varices', 'Varices'),
    ('Audición', 'Audición'),
    ('Sombrero Blanco', 'Sombrero Blanco')
]
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='product_images', blank=True)
    old_price = models.IntegerField(null=True, default=None, blank=True)
    popular = models.BooleanField(default=False)
    category = models.CharField(max_length=255, choices=CATEGORIES, default='Aumento')
    rating = models.IntegerField(default=5)
    link = models.URLField(blank=True)

    def get_sale_percent(self):
        return int((self.old_price - self.price) / self.old_price * 100)
    
    def get_random_amount_of_comments(self):
        return random.randint(50, 200)

    def __str__(self):
        return self.name
    

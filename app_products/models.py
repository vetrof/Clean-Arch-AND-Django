from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()

    def have_discount(self):
        if 100 <= self.price <= 200:
            return True
        return False

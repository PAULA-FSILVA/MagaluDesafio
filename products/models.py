from django.db import models
from seller.models import Seller


status_product = [
        ("A", "Active"),
        ("I", "Inactive"),
    ]


class Product(models.Model):
    title = models.CharField(max_length=250)
    price = models.FloatField()
    id_product = models.IntegerField(unique=True)
    seller = models.ForeignKey(Seller, null=True, on_delete=models.SET_NULL)
    qt_stock = models.PositiveIntegerField()
    status = models.CharField(max_length=1, choices=status_product)

    def to_dict(self):
        return {
            "title": self.title,
            "price": self.price,
            "id_product": self.id_product,
            "seller": self.seller.name,
            "qt_stock": self.qt_stock,
            "status": self.status
        }

    def __str__(self):
        return self.title

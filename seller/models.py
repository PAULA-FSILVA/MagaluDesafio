from django.db import models


class Seller(models.Model):
    name = models.CharField(max_length=200)
    seller_id = models.IntegerField()
    status_product = [
        ("A", "Active"),
        ("I", "Inactive"),
    ]

    def __str__(self):
        return self.name




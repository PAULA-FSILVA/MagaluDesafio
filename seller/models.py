from django.db import models


class Seller(models.Model):
    name = models.CharField(max_length=200)
    seller_id = models.IntegerField()
    status_seller = [
        ("A", "Active"),
        ("I", "Inactive"),
    ]


    def to_dict(self):
        return {
            "name": self.name,
            "seller_id": self.seller_id,
            "status_seller": self.status_seller
        }


    def __str__(self):
        return self.name







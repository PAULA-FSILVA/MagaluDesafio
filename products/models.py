from django.db import models

class Seller(models.Model):
    name = models.CharField(max_length=200)
    seller_id = models.IntegerField()

    def __str__(self):
        return self.name
status_product = [
    ("A", "Active"),
    ("I", "Inactive"),
]

class Product(models.Model):
    title = models.CharField(max_length=250)
    price = models.FloatField()
    id_product = models.IntegerField()
    seller = models.ForeignKey(Seller, null=True,on_delete=models.SET_NULL)
    qt_stock = models.IntegerField()
    status = models.CharField(max_length=1, choices=status_product)



    def to_dict(self):
        print(self.seller)
        return {
            "id": self.id,
            "title": self.title,
            "price": self.price,
            "id_product": self.id_product,
            "seller": self.seller.name,
            "qt_stock": self.qt_stock,
            "status": self.status
        }



    def __str__(self):
        return self.title

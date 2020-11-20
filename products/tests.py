from django.test import TestCase
from seller.models import Seller
from .views import index, detail, create_product
from .models import Product
from unittest.mock import Mock, patch
import json
class ProductModelsTests(TestCase):
    def test_to_dict_when_valid_product_expected_dict(self):
        dict = {
            'title': 'productTitle',
            'price': 1,
            'id_product': 'productId',
            'seller': 'sellerName',
            'qt_stock': 0,
            'status': 'A'
        }
        seller = Seller()
        seller.name = "sellerName"
        product = Product()
        product.title = "productTitle"
        product.price = 1
        product.id_product = "productId"
        product.seller = seller
        product.qt_stock = 0
        product.status = "A"
        self.assertEquals(product.to_dict(), dict)
class ProductViewsTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        seller = Seller()
        seller.name = "sellerName"
        seller.seller_id = 1
        Seller.objects.create(name="sellerName", seller_id=1)
        Product.objects.create(title="cadeira", price="5", id_product="32", qt_stock="8", seller_id=1, status= 'A')
        Product.objects.create(title="mesa", price="15", id_product="8", qt_stock="3", seller_id=1, status= 'A')
        Product.objects.create(title="computador", price="1000", id_product="6", qt_stock="1", seller_id=1, status= 'A')
    def test_index_expected_dict(self):
        data_assert = {'products': [
            {'title': 'cadeira', 'price': 5.0, 'id_product': 32, 'seller': 'sellerName', 'qt_stock': 8, 'status': 'A'},
            {'title': 'computador', 'price': 1000.0, 'id_product': 6, 'seller': 'sellerName', 'qt_stock': 1, 'status': 'A'},
            {'title': 'mesa', 'price': 15.0, 'id_product': 8, 'seller': 'sellerName', 'qt_stock': 3, 'status': 'A'}
        ]}
        request = Mock()
        response = index(request)
        data = json.loads(response.content)
        self.assertEquals(data, data_assert)
    def test_detail_method_get_expected_dict(self):
        data_assert = {'title': 'cadeira', 'price': 5.0, 'id_product': 32, 'seller': 'sellerName', 'qt_stock': 8, 'status': 'A'}
        request = Mock()
        request.method = 'GET'
        response = detail(request, 32)
        data = json.loads(response.content)
        self.assertEquals(data, data_assert)
    def test_detail_method_put_expected_dict(self):
        data_assert = {'title': 'cadeira', 'price': 6.0, 'id_product': 32, 'seller': 'sellerName', 'qt_stock': 8, 'status': 'A'}
        request = Mock()
        request.method = 'PUT'
        request.body = json.dumps(data_assert)
        response = detail(request, 32)
        data = json.loads(response.content)
        self.assertEquals(data, data_assert)
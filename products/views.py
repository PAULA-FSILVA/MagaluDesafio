from django.http import Http404, HttpResponseBadRequest, HttpResponseNotAllowed
from .models import Product
from seller.models import Seller
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
import json

@csrf_exempt
def index(request):
    models = Product.objects.all().order_by('title')
    products = []
    for model in models:
        products.append(model.to_dict())

    output = {"products": products}

    return JsonResponse(output)


@csrf_exempt
def create_product(request):
    payload = json.loads(request.body)
    title = payload.get ("title")
    price = payload.get("price")
    id_product = payload.get ("id_product")
    seller_id = payload.get ("seller_id")
    qt_stock = payload.get ("qt_stock")
    status = payload.get ("status")

    if not title:
        return HttpResponseBadRequest ("Title is required: ")

    try:
        seller = Seller.objects.get(seller_id=seller_id)

        product = Product()
        product.title = title
        product.price = price
        product.id_product = id_product
        product.seller = seller
        product.qt_stock = qt_stock
        product.status = status
        product.save()
        
        output = {"product": product.to_dict()}
        return JsonResponse(output)

    except IntegrityError:
        
        return HttpResponseBadRequest("Produto já existe")

    


@csrf_exempt
def detail(request, id_product):
    try:
        product = Product.objects.get(id_product=id_product)
    except Product.DoesNotExist:
        raise Http404 ("Produto inativo ou em falta. ")

    if request.method == "GET":
        response = {"product": product.to_dict()}

    elif request.method == "PUT":
        payload = json.loads(request.body)
        title = payload.get("title")
        price = payload.get("price")
        id_product = payload.get("id_product")
        seller_id = payload.get("seller_id")
        qt_stock = payload.get("qt_stock")
        status = payload.get("status")

        if title:
            product.title = title
        if price is not None:
            product.price = price
        if id_product:
            product.id_product = id_product
        if seller_id:
            product.seller_id = seller_id
        if qt_stock:
            product.qt_stock = qt_stock
            if qt_stock <= 0:
                return HttpResponseNotAllowed ("Digite um valor válido")
        if status:
            product.status = status
            #aqui que temos que fazer o for pro nativo/inativo?

        product.save()

        response = {"product": product.to_dict()}

    elif request.method == "DELETE":
        product.delete()
        response = {}
    else:
        return HttpResponseNotAllowed(["GET", "PUT", "DELETE"])

    return JsonResponse(product.to_dict())





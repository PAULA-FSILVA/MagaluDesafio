from django.http import Http404, HttpResponseBadRequest, HttpResponseNotAllowed
from .models import Product, Seller
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def index(request):
    if request.method == "GET":
        models = Product.objects.all().order_by('title')

        products = []
        for model in models:
            products.append(model.to_dict())

        output = {"products": products}

    elif request.method == "POST":
        payload = json.loads(request.body)
        title = payload.get ("title")
        price = payload.get("price")
        id_product = payload.get ("id_product")
        seller = payload.get ("seller_id")
        qt_stock = payload.get ("qt_stock")
        status = payload.get ("status")

        if not title:
            return HttpResponseBadRequest ("Title is required: ")

        product = Product()
        product.title = title
        product.price = price
        product.id_product = id_product
        product.seller = seller
        product.qt_stock = qt_stock
        product.status = status
        product.save()

        output = {"product": product.to_dict()}
    else:
        return HttpResponseNotAllowed(["GET", "POST"])



    return JsonResponse(output)

@csrf_exempt
def detail(request, id_product):
    try:
        product = Product.objects.get(pk = id_product)
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
        if status:
            product.status = status

        product.save()

        response = {"product": product.to_dict()}

    elif request.method == "DELETE":
        product.delete()
        response = {}
    else:
        return HttpResponseNotAllowed(["GET", "PUT", "DELETE"])

    return JsonResponse(product.to_dict())
@csrf_exempt
def seller (request):
    if request.method == "GET":
        models = Seller.objects.all().order_by("name")

        sellers = [m. to_dict() for m in models]

        return JsonResponse({"seller": seller})
    elif request.method == "POST":
        payload = json.loads(request.body)
        name = payload.get("name")
        seller_id = payload.get("seller_id")

        seller = Seller()
        seller.name = name
        seller.seller_id = seller_id
        seller.save()

        return JsonResponse ({"sellers": seller.to_dict()})

    else:
        return HttpResponseNotAllowed(["GET", "POST"])


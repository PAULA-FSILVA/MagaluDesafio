from django.http import Http404
from .models import Product
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

def index(request):
    models = Product.objects.all().order_by('title')

    products = []
    for model in models:
        products.append(model.to_dict())

    output = {"products": products}

    return JsonResponse(output)


def detail(request, id_product):
    try:
        product = Product.objects.get(pk = id_product)
    except Product.DoesNotExist:
        raise Http404 ("Produto inativo ou em falta.")

    return JsonResponse(product.to_dict())
    

@csrf_exempt
def create_product (request):
    payload = json.loads(request.body)
    title = payload.get("title")
    price = payload.get("price", 0)
    seller = payload.get("seller")
    qt_stock = payload.get("qt_stock")
    status = payload.get("status")

    #if not name:
    #    return HttpResponseBadRequest("name is required")

    product = Product()
    product.title = title
    product.price = price
    product.seller = seller
    product.qt_stock = qt_stock
    product.status = status
    product.save()

    res = {"product": product.to_dict()}
    return JsonResponse (res)


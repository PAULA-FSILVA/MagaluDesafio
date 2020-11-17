from django.http import Http404
from .models import Product
from django.http import JsonResponse

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
        raise Http404 ("Produto inativo ou em falta. ")

    return JsonResponse(product.to_dict())

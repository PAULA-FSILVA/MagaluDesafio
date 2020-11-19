from django.http.response import JsonResponse
from seller.models import Seller
from django.views.decorators.csrf import csrf_exempt
import json


def get_all(request):
    models = Seller.objects.all().order_by("name")
    sellers = [m. to_dict() for m in models]

    return JsonResponse({"seller": sellers})

def get_one(request, seller_id):
    try:
        seller = Seller.objects.get(seller_id=seller_id)
    except Seller.DoesNotExist:
        raise Http404 ("Seller inexistente ou inativo. ")
    models = Seller.objects.all().order_by('name')

    sellers = []
    for model in models:
        sellers.append(model.to_dict())

    output = {"sellers": seller}

    return JsonResponse(seller)


@csrf_exempt
def post_seller (request):
    payload = json.loads(request.body)
    name = payload.get("name")
    seller_id = payload.get("seller_id")
    #status_seller = payload.get("status_seller")

    seller = Seller()
    seller.name = name
    seller.seller_id = seller_id
    #seller.status_seller= 'A'
    seller.save()

    return JsonResponse ({"sellers": seller.to_dict()})





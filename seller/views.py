from django.http.response import JsonResponse
from .models import Seller
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseNotAllowed
import json



def get_all(request):
    models = Seller.objects.all().order_by("name")
    sellers = [m. to_dict() for m in models]

    return JsonResponse({"seller": sellers})


@csrf_exempt
def post_seller (request):
    payload = json.loads(request.body)
    name = payload.get("name")
    seller_id = payload.get("seller_id")

    seller = Seller()
    seller.name = name
    seller.seller_id = seller_id
    seller.status_seller= 'A'
    seller.save()

    return JsonResponse ({"sellers": seller.to_dict()})

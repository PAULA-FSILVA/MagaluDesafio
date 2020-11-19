from django.http.response import JsonResponse
from .models import Seller
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseNotAllowed
import json



def get_all(request):
    return JsonResponse({"A":"chablau"})

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

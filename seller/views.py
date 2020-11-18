from django.http.response import JsonResponse
from django.shortcuts import render

# Create your views here.

def get_all(request):
    return JsonResponse({"A":"chablau"})
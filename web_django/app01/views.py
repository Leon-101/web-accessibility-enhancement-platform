# Create your views here.
from app01.models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def login(requeset):
    print(requeset.method)
    print(requeset.POST.get("username"))
    return JsonResponse({"code":200})

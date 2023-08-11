import sqlite3
from app01.models import *
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def login(request):
    print(request.method)
    print(request.POST.get("username"))
    return JsonResponse({"code": 200})


def scripts_list(request):
    pass


def scripts_detail(request):
    script_id = request.GET.get("script_id")
    row = Script.objects.filter(id=script_id).first()
    data = {"id": row.id,
            "title": row.title,
            "description": row.description,
            "stars": row.stars,
            "create_time": row.create_time,
            "script_url":row.script_path,
            }

    return JsonResponse(data)

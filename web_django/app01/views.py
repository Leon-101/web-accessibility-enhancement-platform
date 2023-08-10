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
    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()
    script_id=request.GET.get("script_id")
    query=f"select * from scripts where id='{script_id}'"
    print(query)
    cursor.execute(query)
    result=cursor.fetchall()

    for row in result:
        print(row)
    cursor.close()
    conn.close()
    return HttpResponse("ok")

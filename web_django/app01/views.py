from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from app01.models import *


@csrf_exempt
def login(request):
    return JsonResponse({"code": 200})


def scripts_list(request):
    sort_by = request.GET.get("sort_by", "create_time")
    order = "-" if request.GET.get("order", "asc") == "desc" else ""  # 如果是desc是降序，默认升序
    order_by = order + sort_by
    limit = int(request.GET.get("limit", "10"))
    offset = int(request.GET.get("offset", "1"))

    queryset = Script.objects.all().order_by(order_by)[offset - 1:offset - 1 + limit]
    resp_data = []
    for obj in queryset:
        obj_data = {"id": obj.id,
                    "title": obj.title,
                    "description": obj.description,
                    "author": obj.author.username,
                    "stars": obj.stars,
                    "create_time": obj.create_time
                    }
        resp_data.append(obj_data)
    resp = {"data": resp_data}
    return JsonResponse(resp)


def scripts_detail(request):
    script_id = request.GET.get("script_id")
    row = Script.objects.filter(id=script_id).first()
    data = {"id": row.id,
            "title": row.title,
            "description": row.description,
            "stars": row.stars,
            "create_time": row.create_time,
            "script_url": row.script_path,
            }

    return JsonResponse(data)

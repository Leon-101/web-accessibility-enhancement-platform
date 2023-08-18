import datetime
import json

from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django import forms
from app01.models import Need
from app01.utils.scriptContent import scriptInfo


class NeedModelForm(forms.ModelForm):
    class Meta:
        model = Need
        fields = '__all__'

        # error_messages = {
        # }


def needs_list(request):
    sort_by = request.GET.get("sort_by", "create_time")
    order = "-" if request.GET.get("order", "asc") == "desc" else ""  # 如果是desc是降序，默认升序
    order_by = order + sort_by
    limit = int(request.GET.get("limit", "10"))
    offset = int(request.GET.get("offset", "1"))
    data_dict = {}
    q = request.GET.get("q", "")
    if q:
        data_dict["name__contains"] = q

    queryset = Need.objects.filter(**data_dict).order_by(order_by)[offset - 1:offset - 1 + limit]
    resp_data = []
    for obj in queryset:
        obj_data = {"id": obj.id,
                    "name": obj.name,
                    "description": obj.description,
                    "author": obj.author.username,
                    "create_time": obj.create_time
                    }
        resp_data.append(obj_data)
    resp = {"data": resp_data, "total":  Need.objects.count()}
    return JsonResponse(resp)


# def scripts_detail(request):
#     script_id = request.GET.get("script_id")
#     row = Script.objects.filter(id=script_id).first()
#     data = {"id": row.id,
#             "name": row.name,
#             "description": row.description,
#             "stars": row.stars,
#             "create_time": row.create_time,
#             "script_url": row.script_path,
#             "author": row.author_id
#             }
#
#     return JsonResponse(data)


@csrf_exempt
def upload(request):
    if request.method == 'POST':
        request_body = json.loads(request.body)
        c_time = {"create_time": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        form = NeedModelForm(data={**request_body, **c_time})
        if form.is_valid():
            form.save()
            return JsonResponse({"msg": "上传成功"}, status=200)
        return JsonResponse({"errors": form.errors}, status=400)
    return JsonResponse({"msg": "错误"}, status=400)

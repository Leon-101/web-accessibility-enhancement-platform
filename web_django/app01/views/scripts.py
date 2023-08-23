from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django import forms
from django.db.models import Q
from app01.models import Script
from app01.utils.scriptContent import scriptInfo


class ScriptModelForm(forms.ModelForm):
    class Meta:
        model = Script
        fields = '__all__'

        error_messages = {
            # '__all__': {
            #     "invalid": "xxx"
            # },
            'author': {
                'invalid_choice': '脚本的作者未注册。',
            },
        }


def scripts_list(request):
    sort_by = request.GET.get("sort_by", "create_time")
    order = "-" if request.GET.get("order", "asc") == "desc" else ""  # 如果是desc是降序，默认升序
    order_by = order + sort_by
    limit = int(request.GET.get("limit", "10"))
    offset = int(request.GET.get("offset", "1"))
    data_dict = {}
    q = request.GET.get("q", "")

    queryset = Script.objects.filter(
        Q(name__icontains=q) |
        Q(description__icontains=q) |
        Q(author__username__icontains=q)
    ).order_by(order_by)
    resp_data = []
    for obj in queryset[offset - 1:offset - 1 + limit]:
        obj_data = {"id": obj.id,
                    "name": obj.name,
                    "description": obj.description,
                    "author": obj.author.username,
                    "stars": obj.stars,
                    "create_time": obj.create_time
                    }
        resp_data.append(obj_data)
    resp = {"data": resp_data, "total": len(queryset)}

    return JsonResponse(resp)


def scripts_detail(request):
    script_id = request.GET.get("script_id")
    row = Script.objects.filter(id=script_id).first()
    data = {"id": row.id,
            "name": row.name,
            "description": row.description,
            "stars": row.stars,
            "create_time": row.create_time,
            "script_url": row.script_path,
            "author": row.author_id
            }

    return JsonResponse(data)


def insert_match_website(match, script_id):
    """
    将match的url和URL与脚本呢的关系写入数据库，
    :param match:
    :param script_id:
    :return:
    """
    for url in match:
        if not Website.objects.filter(url=url):
            Website.objects.create(url=url)
        website_id = Website.objects.get(url=url).id
        if not ScriptWebsite.objects.filter(**{"website_id": website_id, "script_id": script_id}):
            ScriptWebsite.objects.create(script_id=script_id, website_id=website_id)


@csrf_exempt
def upload(request):
    if request.method == 'POST':
        file = request.FILES['script_file']
        content = file.read().decode("utf-8")
        info = scriptInfo(content)
        info["author"] = request.session.get("info").get("username")
        form = ScriptModelForm(data=info)
        if form.is_valid():
            form.save()
            try:
                insert_match_website(info.get("match"), info.get("id"))
            except Exception as e:
                Script.objects.get(id=info.get("id")).delete()
                print(e)
                return JsonResponse({"msg": "服务器错啦"}, status=503)
            return JsonResponse({"msg": "上传成功"}, status=200)
        return JsonResponse({"errors": form.errors}, status=400)
    return JsonResponse({"msg": "错误"}, status=400)


def star(request):
    pass

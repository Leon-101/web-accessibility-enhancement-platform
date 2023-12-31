import os

from django.core import serializers
from django.http import JsonResponse

from app01.models import *
from app01.utils.encrypt import md5
from app01.utils.scriptContent import scriptInfo


def makedata(request):
    # 先清空
    model_list = [Script, Status, User, Role]
    for m in model_list:
        m.objects.all().delete()
    scripts_dir = "static/scripts"
    for filename in os.listdir(scripts_dir):
        file_path = os.path.join(scripts_dir, filename)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)  # 删除文件
        except Exception as e:
            continue

    Role.objects.create(id=1, name="普通用户")
    Role.objects.create(id=2, name="开发者")
    Role.objects.create(id=3, name="管理员")
    User.objects.create(username="Leon-101", password=md5("123456"), email="123456@qq.com", role_id=2)
    User.objects.create(username="shengrihui", password=md5("666666"), email="1120058252@qq.com", role_id=2)
    Status.objects.create(id=1, status="未审核")
    Status.objects.create(id=2, status="审核未通过")
    Status.objects.create(id=3, status="审核通过")

    # Script
    for i in range(16):
        t = chr(65 + i) * 3
        a = "Leon-101" if i % 2 else "shengrihui"
        script = f"""// ==UserScript==
    // @name         {t}网站无障碍优化脚本
    // @namespace    http://a11y.org
    // @version      0.1
    // @description  优化{t}网站的无障碍问题
    // @author       {a}
    // @match        https://www.baidu.com/*
    // @grant        none
    // ==/UserScript==

    (function () {{
        'use strict';

        setTimeout(() => alert("{t}网站优化已完成~"), 3000);
    }})();
    """
        info = scriptInfo(script)
        Script.objects.create(id=info.get("id"), name=info.get("name", ""),
                              description=info.get("description", ""),
                              author_id=info.get("author", ""), status_id=1, create_time=info.get("create_time"),
                              script_path=info.get("script_path"))
    script_data = Script.objects.all()
    data = serializers.serialize('python', script_data)
    return JsonResponse(data, safe=False)

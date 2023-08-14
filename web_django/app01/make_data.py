from hashlib import md5
import re
import re
from datetime import datetime
from hashlib import md5

from django.core import serializers
from django.http import JsonResponse

from app01.models import *


def makedata(request):
    # 先清空
    model_list = [Script, Status, User, Role]
    for m in model_list:
        m.objects.all().delete()
    Role.objects.create(id=1, name="普通用户")
    Role.objects.create(id=2, name="开发者")
    Role.objects.create(id=3, name="管理员")
    User.objects.create(id=1, username="Leon-101", password=md5("123456".encode()).hexdigest(), email="123456@qq.com",
                        gender=1, role_id=2)
    User.objects.create(id=2, username="shengrihui", password=md5("666666".encode()).hexdigest(),
                        email="1120058252@qq.com", gender=1, role_id=2)
    Status.objects.create(id=1, status="未审核")
    Status.objects.create(id=2, status="审核未通过")
    Status.objects.create(id=3, status="审核通过")

    # Script
    for i in range(16):
        t = chr(65 + i) * 3
        script = f"""// ==UserScript==
    // @name         {t}网站无障碍优化脚本
    // @namespace    http://a11y.org
    // @version      0.1
    // @description  优化{t}网站的无障碍问题
    // @author       {t}
    // @match        https://www.baidu.com/*
    // @grant        none
    // ==/UserScript==

    (function () {{
        'use strict';

        setTimeout(() => alert("{t}网站优化已完成~"), 3000);
    }})();
    """

        script_id = md5((script + str(i)).encode()).hexdigest()
        path = f"static/scripts/{script_id}.js"
        with open(path, "w", encoding="utf-8")as f:
            f.write(script)

        current_datetime = datetime.now()
        date_string = current_datetime.strftime('%Y-%m-%d %H:%M:%S')

        info = dict()
        pattern = r"@(.*?)\n"
        matches = re.findall(pattern, script)
        for match in matches:
            k, v = match.split()
            if k in info:
                # 如果info里已经也了k，
                # 而且它还不是列表的形式，就先将它变成列表
                if isinstance(info[k], str):
                    info[k] = [info[k]]
                info[k].append(v)
            else:
                info[k] = v
        Script.objects.create(id=script_id, title=info.get("name", ""), description=info.get("description", ""),
                              author_id=1, status_id=1, create_time=date_string, script_path=path, )
    script_data = Script.objects.all()
    data = serializers.serialize('python', script_data)
    return JsonResponse(data, safe=False)

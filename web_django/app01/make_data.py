import hashlib
from hashlib import md5
import re
import sqlite3
from datetime import datetime

from django.core import serializers

from app01.models import *
from django.http import HttpResponse, JsonResponse


def makedata(request):
    # 先清空
    model_lsit = [Script]
    for m in model_lsit:
        m.objects.all().delete()

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
        print(script_id)
        print(len(script_id))
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

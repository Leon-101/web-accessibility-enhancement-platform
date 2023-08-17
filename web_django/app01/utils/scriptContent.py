import re
from datetime import datetime

from app01.utils.encrypt import md5


def scriptInfo(content):
    script_id = md5(content)
    path = f"static/scripts/{script_id}.user.js"
    with open(path, "w", encoding="utf-8")as f:
        f.write(content)

    current_datetime = datetime.now()
    date_string = current_datetime.strftime('%Y-%m-%d %H:%M:%S')

    info = {
        "id": script_id,
        "create_time": date_string,
        "script_path": path,
        "match": []
    }
    pattern = r"@(.*?)\n"
    matches = re.findall(pattern, content)
    for match in matches:
        k, v = match.split()
        if k in info:
            if isinstance(info[k], list):
                info[k].append(v)
        else:
            info[k] = v
    return info

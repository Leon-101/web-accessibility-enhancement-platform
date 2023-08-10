import hashlib
import re
import sqlite3
from datetime import datetime
def scripts():

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

        script_id = hashlib.md5((script + str(i)).encode()).hexdigest()

        path = f"static/scripts/{script_id}.js"
        with open(path, "w", encoding="utf-8")as f:
            f.write(script)

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

        current_datetime = datetime.now()
        date_string = current_datetime.strftime('%Y-%m-%d %H:%M:%S')

        cursor.execute("insert into scripts (id,title,author_id,script_path,update_time) values(?,?,?,?,?)",
                       (script_id, info["name"], i, path, date_string))


def user():
    for i in range(25):
        pass
if __name__ == '__main__':
    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()
    # scripts()
    user()
    conn.commit()
    cursor.close()
    conn.close()

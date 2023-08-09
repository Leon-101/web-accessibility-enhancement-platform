import hashlib
import sqlite3
from datetime import datetime
script = """// ==UserScript==
// @name         xxx网站无障碍优化脚本
// @namespace    http://a11y.org
// @version      0.1
// @description  优化xxx网站的无障碍问题
// @author       YYY
// @match        https://www.baidu.com/*
// @grant        none
// ==/UserScript==

(function () {
    'use strict';

    setTimeout(() => alert("xxx网站优化已完成~"), 3000);
})();
"""

conn = sqlite3.connect("db.sqlite3")
cursor = conn.cursor()

# for t in ["audio", "ext_example", "sense", "word", "vocab_example", "word_sense"]:
#     cursor.execute(f"delete from {t} where 1=1")
# cursor.executemany("insert into audio values(?,?,?)", audio_values)
# cursor.executemany("insert into ext_example values(?,?,?,?,?,?,?,?,?,?)", ext_example_values)
# cursor.executemany("insert into sense values(?,?,?,?,?)", sense_values)
# cursor.executemany("insert into word values(?,?,?,?)", word_values)
# cursor.executemany("insert into vocab_example values(?,?,?,?,?,?,?)", vocab_example_values)
# cursor.executemany("insert into word_sense values(?,?)", word_sense_values)
#

for i in range(5):
    script_id = hashlib.md5((script + str(i)).encode()).hexdigest()
    # print(script_id)
    path = f"static/scripts/{script_id}.js"
    with open(path, "w", encoding="utf-8")as f:
        f.write(script)

    current_datetime = datetime.now()
    date_string = current_datetime.strftime('%Y-%m-%d %H:%M:%S')

    cursor.execute("insert into scripts (id,title,author_id,script_path,update_time) values(?,?,?,?,?)",
                   (script_id, "title_" + str(i), i, path,date_string))

conn.commit()
cursor.close()
conn.close()

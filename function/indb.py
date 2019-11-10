import sqlite3

key = ['嵌字', '同人誌', '天鹅之恋', '汉化', '中国語', '漢化', '單行本', '月号', '風的工房', '掃圖', '雑誌寄せ集め', '字幕组', '新桥月白', '掃圖', '翻译',
       '中文',
       '重嵌']
li = []
conn = sqlite3.connect(r'E:\mydb.db')
cursor = conn.cursor()
for i in key:
    li.append((None, i))
cursor.executemany('insert into key values(?,?)', li)
conn.commit()

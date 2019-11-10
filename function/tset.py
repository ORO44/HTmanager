import sqlite3

sql = "SELECT b.name,GROUP_CONCAT(t.name), b.LIKE, b.path FROM (SELECT id, name, LIKE, path FROM book WHERE author = 'asd' ) b LEFT JOIN tag t on	t.id IN (SELECT tag_id FROM book_tag bt WHERE bt.book_id = b.id) group by b.name"
conn = sqlite3.connect('F:/mydb.db')
cursor = conn.cursor()
r = cursor.execute(sql).fetchall()
print(r)

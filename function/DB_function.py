import os
import re
import sqlite3


class DBFunction():
    def __init__(self):
        self.conn = sqlite3.connect(r'.\mydb.db')
        self.cursor = self.conn.cursor()

    def iniDB(self):
        self.cursor.execute('''DROP TABLE IF EXISTS "author";''')
        self.cursor.execute('''DROP TABLE IF EXISTS "book";''')
        self.cursor.execute('''DROP TABLE IF EXISTS "book_tag";''')
        self.cursor.execute('''DROP TABLE IF EXISTS "collection";''')
        self.cursor.execute('''DROP TABLE IF EXISTS "collection_book";''')
        self.cursor.execute('''DROP TABLE IF EXISTS "tag";''')
        self.cursor.execute('''DROP TABLE IF EXISTS "key";''')
        self.cursor.execute('''DROP TABLE IF EXISTS "db_path";''')
        self.cursor.execute('''
        CREATE TABLE "author" (
            "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            "name" TEXT,
            "path" TEXT
        );
        ''')
        self.cursor.execute('''
CREATE TABLE "book" (
  "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  "name" TEXT,
  "like" integer,
  "path" TEXT,
  "author" TEXT
);
        ''')
        self.cursor.execute('''
        CREATE TABLE "book_tag" (
            "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            "book_id" INTEGER,
            "tag_id" INTEGER,
            CONSTRAINT "b" FOREIGN KEY ("book_id") REFERENCES "book" ("id") ON DELETE CASCADE ON UPDATE CASCADE,
            CONSTRAINT "t" FOREIGN KEY ("tag_id") REFERENCES "tag" ("id") ON DELETE CASCADE ON UPDATE CASCADE
        );
        ''')
        self.cursor.execute('''
        CREATE TABLE "collection" (
            "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            "name" TEXT
        );
        ''')
        self.cursor.execute('''
        CREATE TABLE "collection_book" (
            "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            "collection_id" INTEGER,
            "book_id" INTEGER,
            CONSTRAINT "c" FOREIGN KEY ("collection_id") REFERENCES "collection" ("id") ON DELETE CASCADE ON UPDATE CASCADE,
            CONSTRAINT "b2" FOREIGN KEY ("book_id") REFERENCES "book" ("id") ON DELETE CASCADE ON UPDATE CASCADE
        );
        ''')
        self.cursor.execute('''
        CREATE TABLE "tag" (
            "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            "name" TEXT
        );
        ''')
        self.cursor.execute('''CREATE TABLE "db_path" (
  "id" INTEGER NOT NULL,
  "path" TEXT,
  PRIMARY KEY ("id")
);''')
        self.cursor.execute('''
            CREATE TABLE "key" (
              "id" integer NOT NULL,
              "key" TEXT,
              PRIMARY KEY ("id")
            );
        ''')
        self.cursor.execute('''
            INSERT INTO "key" VALUES (1, '嵌字,同人誌,天鹅之恋,汉化,中国語,漢化,單行本,月号,風的工房,掃圖,雑誌寄せ集め,字幕组,新桥月白,掃圖,翻译,中文,重嵌,單行本,天鹅之恋,中国語,天鵝之戀,風與彧製作,黑暗掃圖,MJK,COMIC,脸肿');
        ''')
        self.cursor.execute('''
            insert into "db_path" values  (1,'none')
        ''')
        self.cursor.execute('''UPDATE "sqlite_sequence" SET seq = 1 WHERE name = 'author';''')
        self.cursor.execute('''UPDATE "sqlite_sequence" SET seq = 1 WHERE name = 'collection';''')
        self.cursor.execute('''UPDATE "sqlite_sequence" SET seq = 1 WHERE name = 'tag';''')
        self.conn.commit()

    def new_db(self, path):
        author = os.listdir(path)
        author_path = []
        book_name = []
        book_path = []
        author_data = []
        book_data = []
        for i in author:
            author_path.append(path + '/' + i)
            book_name = os.listdir(path + '/' + i)
            for k in book_name:
                book_path.append(path + '/' + i + '/' + k)
        # author data
        for i in range(len(author)):
            author_data.append((None, author[i], author_path[i]))
        # book data
        for i in range(len(book_name)):
            book_data.append((None, book_name[i], 0, book_path[i], re.findall(r'\[\S+\]', book_name[i])[0]))

        self.cursor.executemany('''insert into author values (?,?,?)''', author_data)
        self.cursor.executemany('''insert into book values (?,?,?,?,?)''', book_data)
        self.conn.commit()

    def creat_tag(self, name):
        self.cursor.execute('''INSERT INTO tag values (?)''', name)
        self.conn.commit()

    def intStartData(self):
        path = self.cursor.execute('''select path from db_path''').fetchall()
        if len(path) > 0:
            author = self.cursor.execute('''select name from author''').fetchall()
            tag = self.cursor.execute('''select name from tag''').fetchall()
            collection = self.cursor.execute('''select name from collection''').fetchall()
            data = []
            if len(author) > 0:
                data.append(author)
            else:
                data.append([])
            if len(tag) > 0:
                data.append(tag)
            else:
                data.append([])
            if len(collection) > 0:
                data.append(collection)
            else:
                data.append([])
            return data
        else:
            return [[], [], []]

    def getAuthorList(self, key):
        sql = """SELECT b.name,GROUP_CONCAT(t.name), b.LIKE, b.path FROM (SELECT id, name, LIKE, path FROM book WHERE author = "{0}" ) b LEFT JOIN tag t on	t.id IN (SELECT tag_id FROM book_tag bt WHERE bt.book_id = b.id) group by b.name""".format(
            key)
        result = self.cursor.execute(sql).fetchall()
        return result

    def getTagList(self, key):
        result = self.cursor.execute(
            """SELECT b.name,GROUP_CONCAT(t.name),b.like,b.path  FROM (select id,name,like,path from book where id in (select book_id from book_tag where tag_id =(SELECT id from tag where name ="{0}"))) b LEFT JOIN tag t on t.id in(select tag_id from book_tag bt where bt.book_id = b.id)  group by b.name""".format(
                key)).fetchall()
        return result

    def getCollectionList(self, key):
        sql = '''SELECT b.name, GROUP_CONCAT(t.name) ,b.like,b.path FROM (select id,name,like,path from book where id in (select book_id from collection_book where collection_id =(SELECT id from collection where name ="{0}"))) b LEFT JOIN tag t on t.id in(select tag_id from book_tag bt where bt.book_id = b.id)  group by b.name'''.format(
            key)
        result = self.cursor.execute(sql).fetchall()
        return result

    def rightMenuEvent(self, table, type, key, update):
        if type == 'add':
            self.cursor.execute('''insert into {0} value (None,?)'''.format(table), key)
        if type == 'del':
            self.cursor.execute('''DELETE from {0} where name="{1}"'''.format(table, key))
        if type == 'rename':
            self.cursor.execute('''DELETE {0} set name="{1}" where name="{2}"'''.format(table, key, update))

    def treeItemUpdate(self, type, old, now):
        if type == '收藏夹':
            table = 'collection'
        if type == '作者':
            table = 'author'
        if type == 'tag':
            table = 'tag'

        sql = '''UPDATE {0} set name = "{1}" where name="{2}"'''.format(table, now, old)
        sql2 = '''UPDATE book set author = "{0}" where author="{1}" '''.format(now, old)
        self.cursor.execute(sql)
        self.cursor.execute(sql2)
        self.conn.commit()

    def FormatData(self, method, data):
        if method == 'get':
            result = self.cursor.execute('''select key from key''').fetchall()
            if len(result) > 0:
                return result[0][0]
        if method == 'update':
            self.cursor.execute('''update key set key ="{0}"'''.format(data))
            self.conn.commit()

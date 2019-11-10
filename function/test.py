import os
import sqlite3
import time


def k():
    conn = sqlite3.connect('E:/mydb.db')
    cursor = conn.cursor()
    # cursor.execute('''insert into author values (?,?)''', ('dsfsdf''dddd'))

    k = cursor.execute('''select key from key''').fetchall()
    r = k[0][0]
    print(r)


if __name__ == '__main__':
    k()

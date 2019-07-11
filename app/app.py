
# -*- coding: utf-8 -*-

import sys
import errno
import os
from flask import Flask
import json
# from sqlalchemy import SQLAlchemy

# from database.core import *
# from database.factory import *
# from springpython.database.core import *
# from springpython.database.factory import *
import MySQLdb

app = Flask(__name__)

locale = 'th'
db = MySQLdb.connect(host="192.168.88.226", port=3306, user="root", passwd="123456")
c = db.cursor()
c.execute('SET NAMES utf8mb4')
c.execute("SET CHARACTER SET utf8mb4")
c.execute("SET character_set_connection=utf8mb4")

c.execute("""select * from eg_product.category_translations where eg_product.category_translations.category_id in (2, 3, 4, 5, 6) and eg_product.category_translations.locale = %s""", (locale,))
rows = c.fetchall()

for row in rows:
    print(row)

c.close()
db.close()


# conn = MySQL.connection(username="root", password="123456", hostname="192.168.88.226")
# cursor = conn.cursor()
# results = []
# try:
#     cursor.execute("select * from eg_product.`category_translations` where eg_product.category_translations.category_id in (2, 3, 4, 5, 6) and eg_product.category_translations.locale = 'th'")
#     for row in cursor.fetchall():
#         print(row)
# finally:
#     try:
#         cursor.close()
#     except Exception:
#         pass
# conn.close()

# connectionFactory = MySQLConnectionFactory(username="root", password="123456", hostname="192.168.88.226")
# dt = DatabaseTemplate(connectionFactory)

# print(dt)
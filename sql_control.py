import MySQLdb
import os
from dotenv import load_dotenv
from item_keywords_list import keywordList
load_dotenv()

connection = MySQLdb.connect(
    host=os.getenv("HOST"),
    user=os.getenv("USERNAME"),
    passwd=os.getenv("PASSWORD"),
    db=os.getenv("DATABASE"),
    ssl_mode="VERIFY_IDENTITY",
    ssl={
        "ca": "/etc/ssl/cert.pem"
    },
)
connection.autocommit(True)

cursor = connection.cursor()
# 创建一个叫items的表, 字段是id, name, typeId, attr, description
# cursor.execute("CREATE TABLE IF NOT EXISTS items (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), typeId INT, attr VARCHAR(255), description VARCHAR(255))")
# 增加战天使之翼(男)的数据

def get_all_items():
    # 从数据库中获取所有待监控数据
    # 返回list
    cursor.execute("SELECT * FROM items")
    result = cursor.fetchall()
    return result

def add_item(name, typeId, attr, description, search_type=0, low_price=9999999999):
    # 向数据库中添加数据
    # search_type: 0: 数据分析打点, 1: 低价监控
    cursor.execute("INSERT INTO items (name, typeId, attr, description, search_type, low_price, deleted) VALUES (%s, %s, %s, %s, %s, 0)", (
        name,
        typeId,
        attr,
        description,
        search_type,
        low_price
    ))

def delete_item(id):
    # 从数据库中删除数据, 逻辑删除
    cursor.execute("UPDATE items SET deleted = 1 WHERE id = %s", (id))

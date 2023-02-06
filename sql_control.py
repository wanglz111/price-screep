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

def get_all_analysis_items():
    # 从数据库中获取所有待监控数据
    # 返回list
    cursor.execute("SELECT * FROM analysis_items")
    result = cursor.fetchall()
    return result

def add_item_to_analysis_items(name, typeId, attr, excludeAttr, description):
    # 向数据库中添加一条待监控数据
    cursor.execute("INSERT INTO analysis_items (name, typeId, attr, excludeAttr, description) VALUES (%s, %s, %s, %s, %s)", (
        name,
        typeId,
        attr,
        excludeAttr,
        description
    ))

def add_price_point(items_id, timestamp, lowest_price, mean_price, weighted_price, price_record):
    # 向数据库中添加一条价格点
    #     create table qqsg.price_points
    # (
    #     id           int auto_increment
    #         primary key,
    #     items_id     int       null,
    #     timestamp    timestamp null,
    #     lowest_price int       null,
    #     mean_price   int       null
    # );

    cursor.execute("INSERT INTO price_points (items_id, timestamp, lowest_price, mean_price, weighted_price, records) VALUES (%s, %s, %s, %s, %s, %s)", (
        items_id,
        timestamp,
        lowest_price,
        mean_price,
        weighted_price,
        price_record
    ))

def get_all_monitor_items():
    # 从数据库中获取所有待监控数据
    # 返回list
    cursor.execute("SELECT * FROM monitor_items")
    result = cursor.fetchall()
    return result

def add_item_to_monitor_items(name, typeId, attr, excludeAttr, description, trigger_price):
    # 向数据库中添加一条待监控数据
    cursor.execute("INSERT INTO monitor_items (name, typeId, attr, excludeAttr, description, trigger_price) VALUES (%s, %s, %s, %s, %s, %s)", (
        name,
        typeId,
        attr,
        excludeAttr,
        description,
        trigger_price
    ))

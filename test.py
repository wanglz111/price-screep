import uuid
import time
from raw_data_requests import get_data
from sql_control import *
from handle_data import price_data, lower_price_trigger

def test_add_item_to_analysis_items():
    raw_data = get_all_analysis_items()
    for item in raw_data:
        print(item[0])

    # add_item_to_analysis_items("炽天使之翼(女)", 1, '', '', '5c')

    # raw_data = get_all_analysis_items()
    # print(raw_data)

def test_uuid():
    print(uuid.uuid4())
    print(int(time.time()))

def test_get_data():
    print(get_data(keyword='关羽')['shopInitData'][0])
    time.sleep(2)
    print(get_data(keyword='张飞')['shopInitData'][0])
    time.sleep(2)
    print(get_data(keyword='赵云')['shopInitData'][0])
    time.sleep(2)
    print(get_data(keyword='马超')['shopInitData'][0])

def test_add_price_point():
    items = get_all_analysis_items()
    # for item in items[:-1]:
    #     data = get_data(keyword=item[1])
    #     time.sleep(2)
    #     print(data)
    data = get_data(keyword=items[-1][1])
    for record in data['boothInitData']:
        print(record['价格'])

def test_price_data():
    items = get_all_analysis_items()
    for item in items:
        time.sleep(2)
        data = get_data(keyword=item[1])
        (lowest_price, mean_price, weighted_price, price_record) = price_data(data)
        price_record = str(price_record)
        add_price_point(item[0], timestamp=int(time.time()), lowest_price=lowest_price, mean_price=mean_price, weighted_price=weighted_price, price_record=price_record)

def test_lower_price_trigger():
    items = get_all_monitor_items()
    for item in items:
        time.sleep(2)
        data = get_data(keyword=item[1])
        lowest_price = lower_price_trigger(data)
        if lowest_price < item[6]:
            print("trigger!")
            # send message

def test_add_trigger_item():
    add_item_to_monitor_items("炽天使之翼(女)", 1, '', '', '5c', 1_000_000_000)

if __name__ == '__main__':
    # test_sql()
    # test_uuid()
    # test_get_data()
    # test_add_price_point()
    test_price_data()
    # test_lower_price_trigger()
    # test_add_trigger_item()
    pass

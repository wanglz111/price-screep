from raw_data_requests import get_data
from sql_control import get_all_analysis_items, add_item_to_analysis_items, add_price_point, get_all_monitor_items
import time
from handle_data import price_data, lower_price_trigger


def record():
    items = get_all_analysis_items()
    for item in items:
        time.sleep(2)
        try:
            data = get_data(keyword=item[1])
        except:
            print("get data error")
            continue
        (lowest_price, mean_price, weighted_price, price_record) = price_data(data)
        price_record = str(price_record)
        add_price_point(item[0], timestamp=int(time.time()), lowest_price=lowest_price,
                        mean_price=mean_price, weighted_price=weighted_price, price_record=price_record)


def price_trigger():
    items = get_all_monitor_items()
    for item in items:
        time.sleep(2)
        try:
            data = get_data(keyword=item[1])
        except:
            print("get data error")
            continue
        lowest_price = lower_price_trigger(data)
        if lowest_price < item[6]:
            print("trigger!")
            # send message


def main():
    # record() 3600s一次, lower_price_trigger() 600s一次
    while True:
        now = int(time.time())
        if now % 3600 == 0:
            record()
        if now % 600 == 0:
            price_trigger()


if __name__ == '__main__':
    record()
    price_trigger()

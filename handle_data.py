def price_data(answer):
    # 平均价格
    price_sum = 0
    price_count = 0
    price_record = []
    # 加权平均价格
    weighted_price_sum = 0
    weighted_price_count = 0

    records = answer['boothInitData']
    if len(records) == 0:
        raise Exception('No records found')

    lowest_price = records[0]['价格']
    for record in records:
        # 平均价格
        price_sum += record['价格']
        price_count += 1
        # 加权平均价格
        weighted_price_sum += int(record['价格']) * int(record['数量'])
        weighted_price_count += int(record['数量'])
        # 记录
        price_record.append(str(record['价格']) + ' * ' + record['数量'])

    mean_price = price_sum / price_count
    weighted_price = weighted_price_sum / weighted_price_count
    return lowest_price, mean_price, weighted_price, price_record

def lower_price_trigger(answer):
    boothInitData_records = answer['boothInitData']

    shopInitData_records = answer['shopInitData']
    if len(shopInitData_records) == 0 and len(boothInitData_records) == 0:
        raise Exception('No records found')
    lowest_price = boothInitData_records[0]['价格'] if boothInitData_records[0]['价格'] < shopInitData_records[0]['jq'] else shopInitData_records[0]['jq']

    return lowest_price
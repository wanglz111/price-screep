import zlib
import requests
import uuid
import time
import hashlib
import base64
import numpy as np
import json

def get_data(keyword='野兽之灵', region='群雄', attr='', excludeAttr='', searchType='exact'):
    uuid_str = uuid.uuid4()
    clientTimestamp = str(int(time.time()))
    data = 'clientGuid=' + str(uuid_str) + '&clientTimestamp=' + clientTimestamp + '&key=6JFzFFN5527IYdDf16VlBxErt96NTX18'
    sign = hashlib.md5(data.encode('utf-8')).hexdigest()

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        'Origin': 'https://qqsg.pc9527.vip',
        'Pragma': 'no-cache',
        'Referer': 'https://qqsg.pc9527.vip/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'type': 'webPage',
    }

    json_data = {
        'keyword': keyword,
        'token': '7ac097cca25e6a4ae0f6411faf537424',
        'userId': 126942,
        'region': region,
        'order': 'asc',
        'attr': attr,
        'excludeAttr': excludeAttr,
        'searchType': searchType,
        'goodsType': '4',
        'clientTimestamp': clientTimestamp,
        'clientGuid': str(uuid_str),
        'sign': sign,
    }

    response = requests.post('https://qqsg.pc9527.vip:3001/qqsg/allList', headers=headers, json=json_data)

    if response.json()['code'] != "200":
        raise Exception('Error: ' + response.json()['msg'])
    # parse response
    code = response.json()['code']
    data = response.json()['data']
    status = response.json()['status']
    message = response.json()['msg']

    # data is base64, convert to string
    raw_data = base64.b64decode(data).decode('utf-8')
    # raw_data is numbers
    raw_data_array = raw_data.split(',')
    # convert to uint8array
    data = [int(i) for i in raw_data_array]
    uint8array = np.array(data, dtype=np.uint8)
    # decompress
    # pako_inflate(uint8array).decode('utf-8')
    # convert to json
    json_data = pako_inflate(uint8array).decode('utf-8')
    answer = json.loads(json_data)
    return answer

    # Note: json_data will not be serialized by requests
    # exactly as it was in the original request.
    #data = '{"keyword":"战天使之翼(男)","token":"7ac097cca25e6a4ae0f6411faf537424","userId":126942,"region":"群雄","order":"asc","attr":"","excludeAttr":"","searchType":"exact","goodsType":"4","clientTimestamp":1675514291,"clientGuid":"2afd6bc9-a219-4d1a-8624-4545a85cb7bd","sign":"0d1d3608365e61d6a0a8cf051ca0cf58"}'.encode()
    #response = requests.post('https://qqsg.pc9527.vip:3001/qqsg/allList', headers=headers, data=data)

def pako_inflate(data):
    decompress = zlib.decompressobj(15)
    decompressed_data = decompress.decompress(data)
    decompressed_data += decompress.flush()
    return decompressed_data

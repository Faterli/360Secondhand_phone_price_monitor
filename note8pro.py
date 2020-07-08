# -*- coding: utf-8 -*-

import time
import json
import traceback

import requests
# 钉钉机器人webhook
webhook = ''
#手机链接URL+目标价格
phones = {
    "6+64":{
        "url":"https://m.bang.360.cn/liangpin/aj_get_goods?brand_id=3&model_id=1385&attr%5B%5D=3641",
        "price":919,
    },
    "6+128":{
        "url":"https://m.bang.360.cn/liangpin/aj_get_goods?brand_id=3&model_id=1385&attr%5B%5D=3642",
        "price":1069,
    },
    "8+128":{
        "url":"https://m.bang.360.cn/liangpin/aj_get_goods?brand_id=3&model_id=1385&attr%5B%5D=3651",
        "price":1169,
    },
}

def send_msg(url, data):
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    requests.packages.urllib3.disable_warnings()
    r = requests.post(url, data=json.dumps(data), headers=headers, verify=False)
    return r.text

try:
    while True:
        for phone in phones:
            response = requests.get(phones[phone]['url'])
            jsonstr = json.loads(response.text)  # json解析响应文本
            # 或者jsonstr = response.json()

            result = jsonstr['result']['good_list']

            for key in result:  # 打印出所有的keys
                if key['price'] < phones[phone]['price']:
                    data = {
                        "msgtype": "text",
                        "text": {
                            "content": "Hi~ %s 的红米note8pro有低价。价格是：%s 元" % (phone,key['price'])
                        },
                        "at": {
                            "atMobiles": [
                                "18888888888",
                            ],
                            "isAtAll": False
                        }
                            }
                    send_msg(webhook, data)

        time.sleep(600)

except :
    pass
# except Exception as e:
#     traceback.print_exc()



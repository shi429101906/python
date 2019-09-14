# coding=utf-8

import base64
import hashlib
import hmac
import json
import time
import logging
import requests

crm_server = 'https://crm.bytedance.com'
pull_clues_api = '/crm/v2/openapi/pull-clues/'


class Signature:
    """ 签名类"""

    def __init__(self, signature_header=None, timestamp_header=None, timeout=None, token_header=None, digestmod=None):
        """
        
        :param signature_header:    签名头部
        :param timestamp_header:    时间戳
        :param timeout:             超时
        :param token_header:        token
        :param digestmod:           加密算法
        """
        self.signature_header = signature_header or 'Signature'
        self.timestamp_header = timestamp_header or 'Timestamp'
        self.token_header = token_header or 'Access-Token'
        self.timeout = timeout or 300
        self.digestmod = digestmod or hashlib.sha256
        self.signature_key = 'SjdOMlM2TFFQOUQ2'
        self.token = '74e7e753e252993e3bc5919785507be0b4b6245d'

    def generate_signature(self, data, key=None):
        key = key if key else self.signature_key

        signature = hmac.new(bytes(key, 'utf-8'), bytes(data, 'utf-8'), digestmod=self.digestmod).digest()
        signature = base64.b64encode(signature)
        return signature


# pagepage_size, page_size10
# start_timeend_time
def crm_pull_clues(start_time, end_time, page=1, page_size=10):
    payload = {}

    payload["start_time"] = start_time
    payload["end_time"] = end_time
    payload["page"] = page
    payload["page_size"] = page_size
    timestamp = str(int(time.time()))
    sig = Signature()
    url = crm_server + pull_clues_api
    data = sig.generate_signature(f'/crm/v2/openapi/pull-clues/?start_time={start_time}&end_time={end_time} {timestamp}')
    headers = {sig.signature_header: data, sig.timestamp_header: timestamp, sig.token_header: sig.token}
    headers.update({'Content-Type': 'application/json'})
    max_tries = 3  # 重试次数
    resp_data = None
    while max_tries > 0:
        try:
            # 打印请求信息
            print('打印请求信息\n', url, '\n', payload, '\n', headers)
            resp = requests.get(url=url, params=payload, headers=headers)
            if resp.status_code == 200:
                res = json.loads(resp.content)  #
                if res:
                    return res
        except Exception as e:
            logging.exception("error with %s" % str(e))
            resp_data = None
        max_tries -= 1
    return resp_data


if __name__ == '__main__':

    res = crm_pull_clues("2018-10-01", "2018-10-30")
    # 打印返回值
    print('\n', '打印返回值')
    print(res)

    if res.get("status") == 0:
        data = res.get("data") or []
        if res.get["count"] > 10:
            count = res.get["count"]
            times = count / 10
            for i in range(times):  # 10
                res = crm_pull_clues("2018-07-01", "2018-07-30", 2 + i)
                data += res.get('data')
        print(len(data))
        print(data)

# coding:utf-8
import time
import hmac
import random
import base64
#import urllib2
import urllib.parse
import requests
# import traceback
from hashlib import sha1

region = 'shanghai'
TCE_SECRET_ID='AKIDylMjqkOq7Azay9Nq8D5kCSVM1Sfft4Sd'
TCE_SECRET_KEY='K8lBONAk7IEzXt30kGXcS5UfbJm0zkG4'

DOMAIN = 'cbs.api3.test.403a.tcecqpoc.fsphere.cn/'
URL = 'http://cbs.api3.test.403a.tcecqpoc.fsphere.cn/?'

def dict2string(d,url=''):
    """
    构造url
    :param d:
    :param url:
    :return:
    """
    requests_string = url
    sort_key = []
    for key,value in d.items():
        sort_key.append(key)
    sort_key.sort()
    for key in sort_key:
        if d.get(key):
            requests_string = requests_string + key+'='+str(d[key])+'&'
    return requests_string[:-1]

def make_signature(method,domain,params):
    """
    生成签名
    :param method:HTTP请求的方法
    :param domain:请求域名
    :param params:请求参数
    :return:签名字符串
    """
    request_string = dict2string(params)
    request_string = method + domain + "?" + request_string
    print('666',request_string)
    hmac_code = hmac.new(TCE_SECRET_KEY.encode(), request_string.encode(), sha1).digest()
    hmac_code = base64.b64encode(hmac_code).decode()
    print('5555',hmac_code)
    return urllib.parse.quote(hmac_code)

def get_instance_state(region):
    params = {
        'Action':'DescribeDisks',
        'Version':'2017-03-12',
        'Nonce':random.randrange(10000),
        'Region':region,
        'SecretId':TCE_SECRET_ID,
        'Timestamp':int(time.time()),
    }
    #params['InstanceIds.0']='ins-bzyqumpd'
    signature = make_signature('GET',DOMAIN,params)
    print('444',signature)
    params['Signature']=signature
    print('3333',signature)
    url =dict2string(params,URL)
    print('1111',url)
    s = requests.session()
#try:
    ret = s.get(url)
    print(ret)
    print(ret.json())

    # except Exception as e:
    #         err_msg = 'HTTP API ERROR\n' + str(e)
    #         print(err_msg)
    #         print(traceback.print_exc(e))

if __name__=="__main__":
    get_instance_state(region)




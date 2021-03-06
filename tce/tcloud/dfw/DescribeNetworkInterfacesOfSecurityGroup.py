# -*- coding: utf8 -*-
from QcloudApi.qcloudapi import QcloudApi
from tce.tcloud.utils.config import global_config

# 设置需要加载的模块
module = 'dfw'

# 对应接口的接口名，请参考wiki文档上对应接口的接口名
action = 'DescribeNetworkInterfacesOfSecurityGroup'
region = global_config.get('regions')
params = global_config.get(region)
secretId = params['secretId']
secretKey = params['secretKey']

# 云API的公共参数
config = {
    'Region': region,
    'secretId': secretId,
    'secretKey': secretKey,
    'method': 'GET',
    'SignatureMethod': 'HmacSHA1'
}

# 接口参数，根据实际情况填写，支持json
# 例如数组可以 "ArrayExample": ["1","2","3"]
# 例如字典可以 "DictExample": {"key1": "value1", "key2": "values2"}
action_params = {
    "sgId":"sg-kj0t6ky2"
}

try:
    service = QcloudApi(module, config)

    # 请求前可以通过下面几个方法重新设置请求的secretId/secretKey/Region/method/SignatureMethod参数
    # 重新设置请求的Region
    # service.setRegion('shanghai')

    # 打印生成的请求URL，不发起请求
    print(service.generateUrl(action, action_params))
    # 调用接口，发起请求，并打印返回结果
    print(service.call(action, action_params))
except Exception as e:
    import traceback

    print('traceback.format_exc():\n%s' % traceback.format_exc())
# -*- coding: utf8 -*-
from QcloudApi.qcloudapi import QcloudApi
from tce.tcloud.utils.server_conf import settings

# 设置需要加载的模块
module = 'lb'

# 对应接口的接口名，请参考wiki文档上对应接口的接口名
action = 'CreateForwardLBSeventhLayerListeners'
Region = 'shanghai'

total_params = settings.get(Region)
# 云API的公共参数
print(total_params['secretId'])
config = {
    'Region': Region,
    'secretId': total_params['secretId'],
    'secretKey': total_params['secretKey'],
    'method': 'GET',
    'SignatureMethod': 'HmacSHA1'
}

# 接口参数，根据实际情况填写，支持json
# 例如数组可以 "ArrayExample": ["1","2","3"]
# 例如字典可以 "DictExample": {"key1": "value1", "key2": "values2"}

action_params = {
    'loadBalancerId':'lb-0wqe13pg',
    'listeners.0.loadBalancerPort':443,
    'listeners.0.protocol':4,
    'listeners.0.SSLMode':'mutual',
    'listeners.0.certName':'myCertName',
    'listeners.0.certContent':'',
    'listeners.0.certKey':'-----BEGIN RSA PRIVATE KEY-----your own key-----END RSA PRIVATE KEY-----',
    'listeners.0.certCaContent':'-----BEGIN CERTIFICATE-----'
                                'MIICwDCCAagCAQEwDQYJKoZIhvcNAQEEBQAwaDELMAkGA1UEBhMCVFgxCzAJBgNVBAgMAlRYMQswCQYDVQQHDAJUWDELMAkGA1UECgwCVFgxCzAJBgNVBAsMAlRYMQsw'
                                'CQYDVQQDDAJUWDEYMBYGCSqGSIb3DQEJARYJVFhAcXEuY29tMB4XDTE5MDEyMjAz'
                                'MDYzMVoXDTIwMDEyMjAzMDYzMVowaDELMAkGA1UEBhMCVFgxCzAJBgNVBAgMAlRYMQswCQYDVQQHDAJUWDELMAkGA1UECgwCVFgxCzAJBgNVBAsMAlRYMQswCQYDVQQD'
                                'DAJUWDEYMBYGCSqGSIb3DQEJARYJVFhAcXEuY29tMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDsiSwcKelWmjH/2oTcKCuq19qE7bd9qBpRdLDRCF/WJrGYpQm9'
                                'J6oikJ55Xhivcy/APcX2C4KtXcUD/MCbZ+nb1J0daWOGmcSkoKhRp/Chp8VGTMJWd6prOC2if/QUbncIVCni6dQE6V86lF6hH8W9ZuncRpgyWMWg9mxdekfQpQIDAQAB'
                                'MA0GCSqGSIb3DQEBBAUAA4IBAQBSVkcG/lIu0O6bEkGj+FBysl45rLa9dt+EKHLL+GKun1lDH6Qz5f7D97SujfH1m8lr1RYsczYjvR1gOr2aRnp7xqJj9pt9Z/VMnXqR'
                                '9djSZHfcnGDCgHlDqXqsIu+L0l9wb/BcjytDpnD5ISEphBGvdj2bFnyva6y/fPwbXk+cdDLY72Xuk8lrk3CBq2qsMg17zDI40Ut0nqcNPPe0BIWip1ernVrW6IhXgD/T'
                                'znwMEWAV9jRtaZcWDkJRfW9YovKsSegu7Y0qQnhtasEyBs1lrdD/W1ohwdS7vc06GlicjYBlpKxelPsvv38Z3v0QPLw9H4e+XPFVAQJOUmR+2PrM-----END CERTIFICATE-----',
    'listeners.0.certCaName':'myCertCaName'


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
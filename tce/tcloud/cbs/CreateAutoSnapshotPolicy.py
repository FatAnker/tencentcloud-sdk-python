# -*- coding: utf-8 -*-
import os
from tce.tcloud.utils.config import global_config
from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
# 导入对应产品模块的client models。
from tencentcloud.cbs.v20170312 import cbs_client, models
import json
# 导入可选配置类
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
region = global_config.get('regions')
params = global_config.get(region)
secretId = params['secretId']
secretKey = params['secretKey']
domain = params['domain']

try:
    # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
    cred = credential.Credential("AKIDylMjqkOq7Azay9Nq8D5kCSVM1Sfft4Sd", "K8lBONAk7IEzXt30kGXcS5UfbJm0zkG4")

    httpProfile = HttpProfile()
    httpProfile.endpoint = "cbs."+domain
    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile

    # 实例化要请求产品(以cvm为例)的client对象，clientProfile是可选的。
    client = cbs_client.CbsClient(cred, region, clientProfile)

    # 实例化一个cvm实例信息查询请求对象,每个接口都会对应一个request对象。
    req = models.CreateAutoSnapshotPolicyRequest()

    # 这里还支持以标准json格式的string来赋值请求参数的方式。下面的代码跟上面的参数赋值是等效的。
    # params =  '{"AutoSnapshotPolicyName":"test_auto_kuaizhao","Policy.0.DayOfWeek.0":["4"],"Policy.0.Hour.0":["0"]}'
    params =  '{"AutoSnapshotPolicyName":"test_auto_kuaizhao","Policy":[{"DayOfWeek":[4],"Hour":[0]}]}'

    req.from_json_string(params)

    resp = client.CreateAutoSnapshotPolicy(req)

    # 输出json格式的字符串回包
    print(resp.to_json_string())

    # 也可以取出单个值。
    # 你可以通过官网接口文档或跳转到response对象的定义处查看返回字段的定义。
    # print(resp.TotalCount)

except TencentCloudSDKException as err:
    print(err)
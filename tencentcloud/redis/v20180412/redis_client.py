# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.redis.v20180412 import models


class RedisClient(AbstractClient):
    _apiVersion = '2018-04-12'
    _endpoint = 'redis.tencentcloudapi.com'


    def Adderror(self, request):
        """asdf

        :param request: 调用Adderror所需参数的结构体。
        :type request: :class:`tencentcloud.redis.v20180412.models.AdderrorRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.AdderrorResponse`

        """
        try:
            params = request._serialize()
            body = self.call("Adderror", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AdderrorResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ClearRedis(self, request):
        """清空Redis实例的实例数据。

        :param request: 调用ClearRedis所需参数的结构体。
        :type request: :class:`tencentcloud.redis.v20180412.models.ClearRedisRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.ClearRedisResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ClearRedis", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ClearRedisResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateRedis(self, request):
        """创建redis实例

        :param request: 调用CreateRedis所需参数的结构体。
        :type request: :class:`tencentcloud.redis.v20180412.models.CreateRedisRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.CreateRedisResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateRedis", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateRedisResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateRedisHour(self, request):
        """按量计费

        :param request: 调用CreateRedisHour所需参数的结构体。
        :type request: :class:`tencentcloud.redis.v20180412.models.CreateRedisHourRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.CreateRedisHourResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateRedisHour", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateRedisHourResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRedis(self, request):
        """查询Redis实例列表

        :param request: 调用DescribeRedis所需参数的结构体。
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeRedisRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeRedisResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRedis", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRedisResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRedisDealDetail(self, request):
        """查询订单详情

        :param request: 调用DescribeRedisDealDetail所需参数的结构体。
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeRedisDealDetailRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeRedisDealDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRedisDealDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRedisDealDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRedisProduct(self, request):
        """本接口查询指定可用区和实例类型下 CRS 的售卖规格， 如果用户不在购买白名单中，将不能查询该可用区或该类型的售卖规格详情。申请购买某地域白名单可以提交工单

        :param request: 调用DescribeRedisProduct所需参数的结构体。
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeRedisProductRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeRedisProductResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRedisProduct", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRedisProductResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRedisRegions(self, request):
        """本接口 (DescribeRegions) 用于查询地域信息。

        :param request: 调用DescribeRedisRegions所需参数的结构体。
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeRedisRegionsRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeRedisRegionsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRedisRegions", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRedisRegionsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRegions(self, request):
        """本接口 (DescribeRegions) 用于查询地域信息。

        :param request: 调用DescribeRegions所需参数的结构体。
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeRegionsRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeRegionsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRegions", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRegionsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTaskInfo(self, request):
        """用于查询任务结果

        :param request: 调用DescribeTaskInfo所需参数的结构体。
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeTaskInfoRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeTaskInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTaskInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTaskInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ExportRedisBackup(self, request):
        """导出CRS实例备份

        :param request: 调用ExportRedisBackup所需参数的结构体。
        :type request: :class:`tencentcloud.redis.v20180412.models.ExportRedisBackupRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.ExportRedisBackupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ExportRedisBackup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ExportRedisBackupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetRedisBackupList(self, request):
        """查询 CRS 实例备份列表

        :param request: 调用GetRedisBackupList所需参数的结构体。
        :type request: :class:`tencentcloud.redis.v20180412.models.GetRedisBackupListRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.GetRedisBackupListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetRedisBackupList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetRedisBackupListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetRedisPerformance(self, request):
        """查看redis实例性能详情

        :param request: 调用GetRedisPerformance所需参数的结构体。
        :type request: :class:`tencentcloud.redis.v20180412.models.GetRedisPerformanceRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.GetRedisPerformanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetRedisPerformance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetRedisPerformanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetRedisSlowLogList(self, request):
        """查询CRS实例慢查询日志列表

        :param request: 调用GetRedisSlowLogList所需参数的结构体。
        :type request: :class:`tencentcloud.redis.v20180412.models.GetRedisSlowLogListRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.GetRedisSlowLogListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetRedisSlowLogList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetRedisSlowLogListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetRedisTaskList(self, request):
        """查询CRS实例的任务列表

        :param request: 调用GetRedisTaskList所需参数的结构体。
        :type request: :class:`tencentcloud.redis.v20180412.models.GetRedisTaskListRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.GetRedisTaskListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetRedisTaskList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetRedisTaskListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def InquiryRedisPrice(self, request):
        """本接口（InquiryRedisPrice）用于查询新购和续费实例价格， 查询升级实例的价格，请参考 查询升级实例价格 。

        :param request: 调用InquiryRedisPrice所需参数的结构体。
        :type request: :class:`tencentcloud.redis.v20180412.models.InquiryRedisPriceRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.InquiryRedisPriceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquiryRedisPrice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquiryRedisPriceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def IsolateRedisInstance(self, request):
        """隔离redis实例

        :param request: 调用IsolateRedisInstance所需参数的结构体。
        :type request: :class:`tencentcloud.redis.v20180412.models.IsolateRedisInstanceRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.IsolateRedisInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("IsolateRedisInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.IsolateRedisInstanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ManualBackupInstance(self, request):
        """手动备份 CRS 实例

        :param request: 调用ManualBackupInstance所需参数的结构体。
        :type request: :class:`tencentcloud.redis.v20180412.models.ManualBackupInstanceRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.ManualBackupInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ManualBackupInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ManualBackupInstanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyRedisName(self, request):
        """修改Redis实例名称

        :param request: 调用ModifyRedisName所需参数的结构体。
        :type request: :class:`tencentcloud.redis.v20180412.models.ModifyRedisNameRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.ModifyRedisNameResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyRedisName", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyRedisNameResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyRedisParams(self, request):
        """修改Redis实例参数

        :param request: 调用ModifyRedisParams所需参数的结构体。
        :type request: :class:`tencentcloud.redis.v20180412.models.ModifyRedisParamsRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.ModifyRedisParamsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyRedisParams", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyRedisParamsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyRedisProject(self, request):
        """修改实例所属项目

        :param request: 调用ModifyRedisProject所需参数的结构体。
        :type request: :class:`tencentcloud.redis.v20180412.models.ModifyRedisProjectRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.ModifyRedisProjectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyRedisProject", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyRedisProjectResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RenewRedis(self, request):
        """续费实例

        :param request: 调用RenewRedis所需参数的结构体。
        :type request: :class:`tencentcloud.redis.v20180412.models.RenewRedisRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.RenewRedisResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RenewRedis", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RenewRedisResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ResetRedisPassword(self, request):
        """重置实例密码

        :param request: 调用ResetRedisPassword所需参数的结构体。
        :type request: :class:`tencentcloud.redis.v20180412.models.ResetRedisPasswordRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.ResetRedisPasswordResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResetRedisPassword", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResetRedisPasswordResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RestoreInstance(self, request):
        """恢复 CRS 实例

        :param request: 调用RestoreInstance所需参数的结构体。
        :type request: :class:`tencentcloud.redis.v20180412.models.RestoreInstanceRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.RestoreInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RestoreInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RestoreInstanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SetRedisAutoRenew(self, request):
        """设置或取消自动续费， 设置自动续费后，系统将在实例到期时，自动发起续费

        :param request: 调用SetRedisAutoRenew所需参数的结构体。
        :type request: :class:`tencentcloud.redis.v20180412.models.SetRedisAutoRenewRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.SetRedisAutoRenewResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SetRedisAutoRenew", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SetRedisAutoRenewResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def Test(self, request):
        """asdf

        :param request: 调用Test所需参数的结构体。
        :type request: :class:`tencentcloud.redis.v20180412.models.TestRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.TestResponse`

        """
        try:
            params = request._serialize()
            body = self.call("Test", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TestResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpgradeRedis(self, request):
        """升级实例

        :param request: 调用UpgradeRedis所需参数的结构体。
        :type request: :class:`tencentcloud.redis.v20180412.models.UpgradeRedisRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.UpgradeRedisResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpgradeRedis", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpgradeRedisResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpgradeRedisInquiryPrice(self, request):
        """查询升级实例价格。

        :param request: 调用UpgradeRedisInquiryPrice所需参数的结构体。
        :type request: :class:`tencentcloud.redis.v20180412.models.UpgradeRedisInquiryPriceRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.UpgradeRedisInquiryPriceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpgradeRedisInquiryPrice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpgradeRedisInquiryPriceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)
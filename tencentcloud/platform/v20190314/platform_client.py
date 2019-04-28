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
from tencentcloud.platform.v20190314 import models


class PlatformClient(AbstractClient):
    _apiVersion = '2019-03-14'
    _endpoint = 'platform.tencentcloudapi.com'


    def DescribePasswords(self, request):
        """获取密码库设备密码

        :param request: 调用DescribePasswords所需参数的结构体。
        :type request: :class:`tencentcloud.platform.v20190314.models.DescribePasswordsRequest`
        :rtype: :class:`tencentcloud.platform.v20190314.models.DescribePasswordsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePasswords", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePasswordsResponse()
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


    def ModifyPassword(self, request):
        """修改设备密码

        :param request: 调用ModifyPassword所需参数的结构体。
        :type request: :class:`tencentcloud.platform.v20190314.models.ModifyPasswordRequest`
        :rtype: :class:`tencentcloud.platform.v20190314.models.ModifyPasswordResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyPassword", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyPasswordResponse()
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


    def Passwords(self, request):
        """获取密码

        :param request: 调用Passwords所需参数的结构体。
        :type request: :class:`tencentcloud.platform.v20190314.models.PasswordsRequest`
        :rtype: :class:`tencentcloud.platform.v20190314.models.PasswordsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("Passwords", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PasswordsResponse()
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


    def QueryPasswords(self, request):
        """查询密码

        :param request: 调用QueryPasswords所需参数的结构体。
        :type request: :class:`tencentcloud.platform.v20190314.models.QueryPasswordsRequest`
        :rtype: :class:`tencentcloud.platform.v20190314.models.QueryPasswordsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("QueryPasswords", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryPasswordsResponse()
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


    def ResetPassword(self, request):
        """重置密码库设备密码

        :param request: 调用ResetPassword所需参数的结构体。
        :type request: :class:`tencentcloud.platform.v20190314.models.ResetPasswordRequest`
        :rtype: :class:`tencentcloud.platform.v20190314.models.ResetPasswordResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResetPassword", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResetPasswordResponse()
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


    def SetPasswordTypes(self, request):
        """重新设置密码类型(长期或临时密码)并修改密码

        :param request: 调用SetPasswordTypes所需参数的结构体。
        :type request: :class:`tencentcloud.platform.v20190314.models.SetPasswordTypesRequest`
        :rtype: :class:`tencentcloud.platform.v20190314.models.SetPasswordTypesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SetPasswordTypes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SetPasswordTypesResponse()
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
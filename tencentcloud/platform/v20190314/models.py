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

from tencentcloud.common.abstract_model import AbstractModel


class DescribePasswordsRequest(AbstractModel):
    """DescribePasswords请求参数结构体

    """

    def __init__(self):
        """
        :param Ips: 设备ip列表，多个用;号分隔
        :type Ips: str
        """
        self.Ips = None


    def _deserialize(self, params):
        self.Ips = params.get("Ips")


class DescribePasswordsResponse(AbstractModel):
    """DescribePasswords返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Filter(AbstractModel):
    """过滤条件

    """

    def __init__(self):
        """
        :param Name: 名称
        :type Name: str
        :param Value: 值
        :type Value: str
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")


class ModifyPasswordRequest(AbstractModel):
    """ModifyPassword请求参数结构体

    """

    def __init__(self):
        """
        :param Filter: 设备名称和密码
        :type Filter: list of Filter
        :param AutoPwd: 自动生成密码
        :type AutoPwd: int
        """
        self.Filter = None
        self.AutoPwd = None


    def _deserialize(self, params):
        if params.get("Filter") is not None:
            self.Filter = []
            for item in params.get("Filter"):
                obj = Filter()
                obj._deserialize(item)
                self.Filter.append(obj)
        self.AutoPwd = params.get("AutoPwd")


class ModifyPasswordResponse(AbstractModel):
    """ModifyPassword返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class PasswordsRequest(AbstractModel):
    """Passwords请求参数结构体

    """

    def __init__(self):
        """
        :param Filter: 查询条件
        :type Filter: list of Filter
        """
        self.Filter = None


    def _deserialize(self, params):
        if params.get("Filter") is not None:
            self.Filter = []
            for item in params.get("Filter"):
                obj = Filter()
                obj._deserialize(item)
                self.Filter.append(obj)


class PasswordsResponse(AbstractModel):
    """Passwords返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class QueryPasswordsRequest(AbstractModel):
    """QueryPasswords请求参数结构体

    """

    def __init__(self):
        """
        :param Filter: 查询条件
        :type Filter: list of Filter
        """
        self.Filter = None


    def _deserialize(self, params):
        if params.get("Filter") is not None:
            self.Filter = []
            for item in params.get("Filter"):
                obj = Filter()
                obj._deserialize(item)
                self.Filter.append(obj)


class QueryPasswordsResponse(AbstractModel):
    """QueryPasswords返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResetPasswordRequest(AbstractModel):
    """ResetPassword请求参数结构体

    """

    def __init__(self):
        """
        :param Ips: ip列表，多个ip用;号分隔
        :type Ips: str
        """
        self.Ips = None


    def _deserialize(self, params):
        self.Ips = params.get("Ips")


class ResetPasswordResponse(AbstractModel):
    """ResetPassword返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ServerDevice(AbstractModel):
    """设备信息

    """

    def __init__(self):
        """
        :param DeviceId: 设备id
        :type DeviceId: str
        :param Password: 密码
        :type Password: str
        :param IntranetIp: 设备ip
        :type IntranetIp: str
        """
        self.DeviceId = None
        self.Password = None
        self.IntranetIp = None


    def _deserialize(self, params):
        self.DeviceId = params.get("DeviceId")
        self.Password = params.get("Password")
        self.IntranetIp = params.get("IntranetIp")


class SetPasswordTypesRequest(AbstractModel):
    """SetPasswordTypes请求参数结构体

    """

    def __init__(self):
        """
        :param Servers: 设备信息列表
        :type Servers: list of ServerDevice
        :param PasswordType: 密码类型
        :type PasswordType: int
        :param AutoPwd: 是否自动生成密码
        :type AutoPwd: int
        """
        self.Servers = None
        self.PasswordType = None
        self.AutoPwd = None


    def _deserialize(self, params):
        if params.get("Servers") is not None:
            self.Servers = []
            for item in params.get("Servers"):
                obj = ServerDevice()
                obj._deserialize(item)
                self.Servers.append(obj)
        self.PasswordType = params.get("PasswordType")
        self.AutoPwd = params.get("AutoPwd")


class SetPasswordTypesResponse(AbstractModel):
    """SetPasswordTypes返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
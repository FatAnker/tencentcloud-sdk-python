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


class AccountInfo(AbstractModel):
    """实例账号信息详情

    """

    def __init__(self):
        """
        :param Account: 账号名字
        :type Account: str
        :param Password: 账号密码
        :type Password: str
        :param AuthRoles: 账号权限列表
        :type AuthRoles: list of Auth
        :param CreateTime: 账号创建时间
        :type CreateTime: str
        :param UpdateTime: 账号更新时间
        :type UpdateTime: str
        :param AccountDesc: 账号描述
        :type AccountDesc: list of str
        """
        self.Account = None
        self.Password = None
        self.AuthRoles = None
        self.CreateTime = None
        self.UpdateTime = None
        self.AccountDesc = None


    def _deserialize(self, params):
        self.Account = params.get("Account")
        self.Password = params.get("Password")
        if params.get("AuthRoles") is not None:
            self.AuthRoles = []
            for item in params.get("AuthRoles"):
                obj = Auth()
                obj._deserialize(item)
                self.AuthRoles.append(obj)
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.AccountDesc = params.get("AccountDesc")


class Auth(AbstractModel):
    """用于控制账号对数据库的读写权限

    """

    def __init__(self):
        """
        :param NameSpace: *表示所有数据库,db.name表示特定的name数据库。
        :type NameSpace: str
        :param Mask: 用于控制权限,0无权限，1只读，2只写，3读写。
        :type Mask: str
        """
        self.NameSpace = None
        self.Mask = None


    def _deserialize(self, params):
        self.NameSpace = params.get("NameSpace")
        self.Mask = params.get("Mask")


class BackupInfo(AbstractModel):
    """用于描述备份信息

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cmgo-p8vnipr5，与云数据库控制台页面中显示的实例ID相同，可使用查询实例列表接口获取，其值为输出参数中字段 InstanceId 的值
        :type InstanceId: str
        :param BackupType: 备份类型，0自动备份，1手动备份
        :type BackupType: int
        :param BackupNum: 备份数,目前固定为1
        :type BackupNum: int
        :param BackupName: 备份名字
        :type BackupName: str
        :param BackupDesc: 备份备注信息
        :type BackupDesc: str
        :param BackupSize: 备份大小
        :type BackupSize: int
        :param StartTime: 开始备份时间
        :type StartTime: str
        :param EndTime: 结束备份时间
        :type EndTime: str
        :param CostTime: 备份耗时
        :type CostTime: list of str
        :param Locked: 是否锁定
        :type Locked: int
        :param Locker: 备份流程Id
        :type Locker: int
        :param LockerDesc: 备份流程描述
        :type LockerDesc: str
        :param Status: 备份状态
        :type Status: int
        :param CreateTime: 备份创建时间
        :type CreateTime: str
        :param UpdateTime: 备份更新时间
        :type UpdateTime: str
        """
        self.InstanceId = None
        self.BackupType = None
        self.BackupNum = None
        self.BackupName = None
        self.BackupDesc = None
        self.BackupSize = None
        self.StartTime = None
        self.EndTime = None
        self.CostTime = None
        self.Locked = None
        self.Locker = None
        self.LockerDesc = None
        self.Status = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BackupType = params.get("BackupType")
        self.BackupNum = params.get("BackupNum")
        self.BackupName = params.get("BackupName")
        self.BackupDesc = params.get("BackupDesc")
        self.BackupSize = params.get("BackupSize")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.CostTime = params.get("CostTime")
        self.Locked = params.get("Locked")
        self.Locker = params.get("Locker")
        self.LockerDesc = params.get("LockerDesc")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")


class ChargeItem(AbstractModel):
    """价格单元

    """

    def __init__(self):
        """
        :param ChargeDesc: 价格描述
        :type ChargeDesc: str
        :param Price: 价格
        :type Price: float
        :param ChargeUnit: 价格单位
        :type ChargeUnit: str
        """
        self.ChargeDesc = None
        self.Price = None
        self.ChargeUnit = None


    def _deserialize(self, params):
        self.ChargeDesc = params.get("ChargeDesc")
        self.Price = params.get("Price")
        self.ChargeUnit = params.get("ChargeUnit")


class CheckAccountPasswordRequest(AbstractModel):
    """CheckAccountPassword请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cmgo-p8vnipr5，与云数据库控制台页面中显示的实例ID相同，可使用查询实例列表接口获取，其值为输出参数中字段 InstanceId 的值
        :type InstanceId: str
        :param Account: 实例账号名字，在实例的账号管理页面下可以看到，比如常用的mongouser。
        :type Account: str
        :param Password: 实例对应账号的密码。
        :type Password: str
        """
        self.InstanceId = None
        self.Account = None
        self.Password = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Account = params.get("Account")
        self.Password = params.get("Password")


class CheckAccountPasswordResponse(AbstractModel):
    """CheckAccountPassword返回参数结构体

    """

    def __init__(self):
        """
        :param IsPassCheck: 描述是否校验正确
        :type IsPassCheck: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.IsPassCheck = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IsPassCheck = params.get("IsPassCheck")
        self.RequestId = params.get("RequestId")


class CreateAccountRequest(AbstractModel):
    """CreateAccount请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cmgo-p8vnipr5，与云数据库控制台页面中显示的实例ID相同，可使用查询实例列表接口获取，其值为输出参数中字段 InstanceId 的值
        :type InstanceId: str
        :param Account: 实例账号名字，在实例的账号管理页面下可以看到，比如常用的mongouser。
        :type Account: str
        :param Password: 实例密码，和实例账号一起用于数据库实例的访问。
        :type Password: str
        :param AuthRoles: 账号授权信息，可以分别对各个数据库分别授权。
        :type AuthRoles: list of Auth
        :param AccountDesc: 账号描述信息。
        :type AccountDesc: str
        """
        self.InstanceId = None
        self.Account = None
        self.Password = None
        self.AuthRoles = None
        self.AccountDesc = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Account = params.get("Account")
        self.Password = params.get("Password")
        if params.get("AuthRoles") is not None:
            self.AuthRoles = []
            for item in params.get("AuthRoles"):
                obj = Auth()
                obj._deserialize(item)
                self.AuthRoles.append(obj)
        self.AccountDesc = params.get("AccountDesc")


class CreateAccountResponse(AbstractModel):
    """CreateAccount返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 流程ID，用于后续查询流程进度。
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class CreateDBInstanceHourRequest(AbstractModel):
    """CreateDBInstanceHour请求参数结构体

    """

    def __init__(self):
        """
        :param Memory: 实例内存大小，单位：MB，请使用[查询可创建规格（支持可用区、配置自定义）](https://cloud.tencent.com/document/api/253/6109)接口获取可创建的内存规格
        :type Memory: int
        :param Volume: 实例硬盘大小，单位：GB，请使用[查询可创建规格（支持可用区、配置自定义）](https://cloud.tencent.com/document/api/253/6109)接口获取可创建的硬盘范围
        :type Volume: int
        :param ReplicateSetNum: 副本集个数，1为单副本集实例，大于1为分片集群实例，最大不超过10
        :type ReplicateSetNum: int
        :param SecondaryNum: 每个副本集内从节点个数，目前只支持从节点数为2
        :type SecondaryNum: int
        :param EngineVersion: MongoDB引擎版本，值包括：3.2wt、3.2rocks和3.6wt，请使用[查询可创建规格（支持可用区、配置自定义）](https://cloud.tencent.com/document/api/253/6109)接口获取可创建的实例版本
        :type EngineVersion: str
        :param Machine: 实例类型，GIO：高IO版；TGIO：高IO万兆
        :type Machine: str
        :param GoodsNum: 实例数量，默认值为1, 最小值1，最大值为10
        :type GoodsNum: int
        :param Zone: 可用区信息，该参数缺省时，系统会自动选择一个可用区，请使用[查询可创建规格（支持可用区、配置自定义）](https://cloud.tencent.com/document/api/253/6109)接口获取可创建的可用区
        :type Zone: str
        :param VpcId: 私有网络ID，如果不传则默认选择基础网络，请使用[查询私有网络列表](/doc/api/245/1372)
        :type VpcId: str
        :param InstanceType: 实例类型，REPLSET：副本集集群；SHARD：分片集群；DYNAMODB：DYNAMODB集群。默认值：REPLSET
        :type InstanceType: str
        :param Encrypt: 数据是否加密，当且仅当引擎版本为3.2rocks，可以选择加密
        :type Encrypt: int
        :param SubnetId: 私有网络下的子网ID，如果设置了 UniqVpcId，则 UniqSubnetId 必填，请使用[查询子网列表](/doc/api/245/1371)
        :type SubnetId: str
        :param ProjectId: 项目ID，不填为默认项目。请使用[查询项目列表](https://cloud.tencent.com/document/product/378/4400)接口获取项目ID
        :type ProjectId: int
        :param Password: 设置管理员帐号密码，密码规则：8-64个字符，至少包含字母、数字、字符（支持的字符：_+-&=!@#$%^*()）中的两种，购买主实例时可指定该参数，购买只读实例或者灾备实例时指定该参数无意义
        :type Password: str
        :param InstanceName: 实例名称
        :type InstanceName: str
        :param SecurityGroup: 安全组参数
        :type SecurityGroup: list of str
        :param InstanceRole: 实例类型，默认为 MASTER，支持值包括：MASTER-表示主实例，DR-表示灾备实例，RO-表示只读实例
        :type InstanceRole: str
        :param MasterInstanceId: 实例ID，购买只读实例或者灾备实例时必填，该字段表示只读实例或者灾备实例的主实例ID，请使用[查询实例列表](https://cloud.tencent.com/document/api/236/15872)接口查询云数据库实例ID
        :type MasterInstanceId: str
        """
        self.Memory = None
        self.Volume = None
        self.ReplicateSetNum = None
        self.SecondaryNum = None
        self.EngineVersion = None
        self.Machine = None
        self.GoodsNum = None
        self.Zone = None
        self.VpcId = None
        self.InstanceType = None
        self.Encrypt = None
        self.SubnetId = None
        self.ProjectId = None
        self.Password = None
        self.InstanceName = None
        self.SecurityGroup = None
        self.InstanceRole = None
        self.MasterInstanceId = None


    def _deserialize(self, params):
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        self.ReplicateSetNum = params.get("ReplicateSetNum")
        self.SecondaryNum = params.get("SecondaryNum")
        self.EngineVersion = params.get("EngineVersion")
        self.Machine = params.get("Machine")
        self.GoodsNum = params.get("GoodsNum")
        self.Zone = params.get("Zone")
        self.VpcId = params.get("VpcId")
        self.InstanceType = params.get("InstanceType")
        self.Encrypt = params.get("Encrypt")
        self.SubnetId = params.get("SubnetId")
        self.ProjectId = params.get("ProjectId")
        self.Password = params.get("Password")
        self.InstanceName = params.get("InstanceName")
        self.SecurityGroup = params.get("SecurityGroup")
        self.InstanceRole = params.get("InstanceRole")
        self.MasterInstanceId = params.get("MasterInstanceId")


class CreateDBInstanceHourResponse(AbstractModel):
    """CreateDBInstanceHour返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateManualBackupRequest(AbstractModel):
    """CreateManualBackup请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cmgo-p8vnipr5，与云数据库控制台页面中显示的实例ID相同，可使用查询实例列表接口获取，其值为输出参数中字段 InstanceId 的值
        :type InstanceId: str
        :param BackupName: 手动备份名字
        :type BackupName: str
        :param BackupRemark: 备份说明
        :type BackupRemark: str
        """
        self.InstanceId = None
        self.BackupName = None
        self.BackupRemark = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BackupName = params.get("BackupName")
        self.BackupRemark = params.get("BackupRemark")


class CreateManualBackupResponse(AbstractModel):
    """CreateManualBackup返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 任务Id
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class DBCollectionInfo(AbstractModel):
    """描述DB名字以及这个DB包含的所有Collection列表

    """

    def __init__(self):
        """
        :param DBName: DB名字
        :type DBName: str
        :param Collections: Collection列表
        :type Collections: list of str
        """
        self.DBName = None
        self.Collections = None


    def _deserialize(self, params):
        self.DBName = params.get("DBName")
        self.Collections = params.get("Collections")


class DeleteAccountRequest(AbstractModel):
    """DeleteAccount请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cmgo-p8vnipr5，与云数据库控制台页面中显示的实例ID相同，可使用查询实例列表接口获取，其值为输出参数中字段 InstanceId 的值
        :type InstanceId: str
        :param Account: 实例账号名字，在实例的账号管理页面下可以看到，比如常用的mongouser。
        :type Account: str
        """
        self.InstanceId = None
        self.Account = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Account = params.get("Account")


class DeleteAccountResponse(AbstractModel):
    """DeleteAccount返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 流水号Id
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class DescribeAccountsRequest(AbstractModel):
    """DescribeAccounts请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cmgo-p8vnipr5，与云数据库控制台页面中显示的实例ID相同，可使用查询实例列表接口获取，其值为输出参数中字段 InstanceId 的值
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class DescribeAccountsResponse(AbstractModel):
    """DescribeAccounts返回参数结构体

    """

    def __init__(self):
        """
        :param Accounts: 账号信息数组
        :type Accounts: list of AccountInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Accounts = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Accounts") is not None:
            self.Accounts = []
            for item in params.get("Accounts"):
                obj = AccountInfo()
                obj._deserialize(item)
                self.Accounts.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBackupsRequest(AbstractModel):
    """DescribeBackups请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cmgo-p8vnipr5，与云数据库控制台页面中显示的实例ID相同，可使用查询实例列表接口获取，其值为输出参数中字段 InstanceId 的值
        :type InstanceId: str
        :param Limit: 显示页面数量
        :type Limit: int
        :param Offset: 页码
        :type Offset: int
        :param OrderBy: 排序规则:backupname,backupsize,starttime,endtime
        :type OrderBy: str
        :param OrderDirection: 排序类型:desc,asc
        :type OrderDirection: str
        :param SerachKey: 查询关键字
        :type SerachKey: str
        :param StartTime: 查询开始时间
        :type StartTime: str
        :param EndTime: 查询结束时间
        :type EndTime: str
        """
        self.InstanceId = None
        self.Limit = None
        self.Offset = None
        self.OrderBy = None
        self.OrderDirection = None
        self.SerachKey = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.OrderBy = params.get("OrderBy")
        self.OrderDirection = params.get("OrderDirection")
        self.SerachKey = params.get("SerachKey")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class DescribeBackupsResponse(AbstractModel):
    """DescribeBackups返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 查询到的备份数目
        :type TotalCount: int
        :param Backups: 备份信息列表
        :type Backups: list of BackupInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Backups = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Backups") is not None:
            self.Backups = []
            for item in params.get("Backups"):
                obj = BackupInfo()
                obj._deserialize(item)
                self.Backups.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCollectionsRequest(AbstractModel):
    """DescribeCollections请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cmgo-p8vnipr5，与云数据库控制台页面中显示的实例ID相同，可使用查询实例列表接口获取，其值为输出参数中字段 InstanceId 的值
        :type InstanceId: str
        :param DescribeTime: 时间戳
        :type DescribeTime: str
        """
        self.InstanceId = None
        self.DescribeTime = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.DescribeTime = params.get("DescribeTime")


class DescribeCollectionsResponse(AbstractModel):
    """DescribeCollections返回参数结构体

    """

    def __init__(self):
        """
        :param DBs: 数据库集合列表
        :type DBs: list of DBCollectionInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DBs = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DBs") is not None:
            self.DBs = []
            for item in params.get("DBs"):
                obj = DBCollectionInfo()
                obj._deserialize(item)
                self.DBs.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBInstancesRequest(AbstractModel):
    """DescribeDBInstances请求参数结构体

    """

    def __init__(self):
        """
        :param ProjectIds: 项目ID
        :type ProjectIds: list of int non-negative
        :param InstanceType: 实例类型，REPLSET：副本集集群；SHARD：分片集群；DYNAMODB：DYNAMODB集群。默认值：REPLSET
        :type InstanceType: str
        :param Vips: 实例的内网IP地址
        :type Vips: list of str
        :param Status: 实例状态，0-待初始化；1-流程处理中；2-运行中；-2-已隔离。
        :type Status: list of int non-negative
        :param Offset: 记录偏移量，默认值为0
        :type Offset: int
        :param Limit: 单次请求返回的数量，默认值为20，最大值为100
        :type Limit: int
        :param OrderBy: 实例状态，一个或者多个状态值，n表示从0开始的数组下标，值包括： 0-待初始化 1-流程中 2-运行中 -2-实例已隔离
        :type OrderBy: str
        :param OrderDirection: 排序字段，支持实例ID（InstanceId）、项目ID（ProjectId）、创建时间（CreateTime）、到期时间（DeadlineTime）及实例名称（InstanceName）进行排序。
        :type OrderDirection: str
        :param InstanceChargeType: 付费类型，PREPAID：预付费，即包年包月；POSTPAID_BY_HOUR：按小时后付费。
        :type InstanceChargeType: str
        :param InstanceIds: 实例ID
        :type InstanceIds: list of str
        :param SerachKey: 模糊匹配字段，支持根据实例名称、实例Id或实例ip进行模糊查找
        :type SerachKey: str
        :param VpcId: vpcID
        :type VpcId: str
        :param SubnetId: 子网ID
        :type SubnetId: str
        :param InstanceRole: 实例类型，默认为 master，支持值包括：master-表示主实例，dr-表示灾备实例，ro-表示只读实例,temp-回档后临时实例
        :type InstanceRole: str
        """
        self.ProjectIds = None
        self.InstanceType = None
        self.Vips = None
        self.Status = None
        self.Offset = None
        self.Limit = None
        self.OrderBy = None
        self.OrderDirection = None
        self.InstanceChargeType = None
        self.InstanceIds = None
        self.SerachKey = None
        self.VpcId = None
        self.SubnetId = None
        self.InstanceRole = None


    def _deserialize(self, params):
        self.ProjectIds = params.get("ProjectIds")
        self.InstanceType = params.get("InstanceType")
        self.Vips = params.get("Vips")
        self.Status = params.get("Status")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OrderBy = params.get("OrderBy")
        self.OrderDirection = params.get("OrderDirection")
        self.InstanceChargeType = params.get("InstanceChargeType")
        self.InstanceIds = params.get("InstanceIds")
        self.SerachKey = params.get("SerachKey")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.InstanceRole = params.get("InstanceRole")


class DescribeDBInstancesResponse(AbstractModel):
    """DescribeDBInstances返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合查询条件的实例总数
        :type TotalCount: int
        :param Items: 实例详细信息
        :type Items: list of InstanceInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = InstanceInfo()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDatabasesRequest(AbstractModel):
    """DescribeDatabases请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cmgo-p8vnipr5，与云数据库控制台页面中显示的实例ID相同，可使用查询实例列表接口获取，其值为输出参数中字段 InstanceId 的值
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class DescribeDatabasesResponse(AbstractModel):
    """DescribeDatabases返回参数结构体

    """

    def __init__(self):
        """
        :param DBs: 数据库名字列表
        :type DBs: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DBs = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DBs = params.get("DBs")
        self.RequestId = params.get("RequestId")


class DescribeOplogsRequest(AbstractModel):
    """DescribeOplogs请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cmgo-p8vnipr5，与云数据库控制台页面中显示的实例ID相同，可使用查询实例列表接口获取，其值为输出参数中字段 InstanceId 的值
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class DescribeOplogsResponse(AbstractModel):
    """DescribeOplogs返回参数结构体

    """

    def __init__(self):
        """
        :param Oplogs: Oplog日志列表
        :type Oplogs: list of Oplog
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Oplogs = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Oplogs") is not None:
            self.Oplogs = []
            for item in params.get("Oplogs"):
                obj = Oplog()
                obj._deserialize(item)
                self.Oplogs.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeReadonlyDelayRequest(AbstractModel):
    """DescribeReadonlyDelay请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cmgo-p8vnipr5，与云数据库控制台页面中显示的实例ID相同，可使用查询实例列表接口获取，其值为输出参数中字段 InstanceId 的值
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class DescribeReadonlyDelayResponse(AbstractModel):
    """DescribeReadonlyDelay返回参数结构体

    """

    def __init__(self):
        """
        :param Stage: 同步阶段: 1全量同步中，2增量同步中
        :type Stage: int
        :param OplogDelay: 增量同步时为主从延时
        :type OplogDelay: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Stage = None
        self.OplogDelay = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Stage = params.get("Stage")
        self.OplogDelay = params.get("OplogDelay")
        self.RequestId = params.get("RequestId")


class DescribeRequestResultRequest(AbstractModel):
    """DescribeRequestResult请求参数结构体

    """

    def __init__(self):
        """
        :param AsyncRequestId: 任务ID
        :type AsyncRequestId: str
        """
        self.AsyncRequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")


class DescribeRequestResultResponse(AbstractModel):
    """DescribeRequestResult返回参数结构体

    """

    def __init__(self):
        """
        :param Status: 任务状态，不传值则查询所有任务状态，可能的值：-1-未定义；0-初始化; 1-运行中；2-执行成功；3-执行失败；4-已终止；5-已删除；6-已暂停；
        :type Status: int
        :param StartTime: 任务的开始时间，时间格式如：2017-12-31 10:40:01
        :type StartTime: str
        :param EndTime: 任务的结束时间，时间格式如：2017-12-31 10:40:01，只有任务状态为执行成功，该字段有效，否则为0000-00-00 00:00:00
        :type EndTime: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.StartTime = None
        self.EndTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.RequestId = params.get("RequestId")


class DescribeRestoreableRequest(AbstractModel):
    """DescribeRestoreable请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cmgo-p8vnipr5，与云数据库控制台页面中显示的实例ID相同，可使用查询实例列表接口获取，其值为输出参数中字段 InstanceId 的值
        :type InstanceId: str
        :param DescribeTime: 回档时间点
        :type DescribeTime: str
        """
        self.InstanceId = None
        self.DescribeTime = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.DescribeTime = params.get("DescribeTime")


class DescribeRestoreableResponse(AbstractModel):
    """DescribeRestoreable返回参数结构体

    """

    def __init__(self):
        """
        :param Restoreable: 是否可回档到这个时间点
        :type Restoreable: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Restoreable = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Restoreable = params.get("Restoreable")
        self.RequestId = params.get("RequestId")


class DescribeSaleInfoRequest(AbstractModel):
    """DescribeSaleInfo请求参数结构体

    """


class DescribeSaleInfoResponse(AbstractModel):
    """DescribeSaleInfo返回参数结构体

    """

    def __init__(self):
        """
        :param TimeSpan: 可售卖时长，单位为月，该参数只对包年包月有效
        :type TimeSpan: int
        :param GoodsList: 可售商品信息
        :type GoodsList: list of ScanAppInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TimeSpan = None
        self.GoodsList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TimeSpan = params.get("TimeSpan")
        if params.get("GoodsList") is not None:
            self.GoodsList = []
            for item in params.get("GoodsList"):
                obj = ScanAppInfo()
                obj._deserialize(item)
                self.GoodsList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSlowPatternsRequest(AbstractModel):
    """DescribeSlowPatterns请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cmgo-p8vnipr5，与云数据库控制台页面中显示的实例ID相同，可使用查询实例列表接口获取，其值为输出参数中字段 InstanceId 的值
        :type InstanceId: str
        :param StartTime: 开始时间
        :type StartTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        :param QueryMaxTime: 查询最大耗时
        :type QueryMaxTime: int
        :param Limit: 返回记录数量
        :type Limit: int
        :param Offset: 偏移
        :type Offset: int
        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.QueryMaxTime = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.QueryMaxTime = params.get("QueryMaxTime")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeSlowPatternsResponse(AbstractModel):
    """DescribeSlowPatterns返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 总条数
        :type TotalCount: int
        :param SlowParttens: 慢查询模式列表
        :type SlowParttens: list of SlowPartten
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.SlowParttens = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("SlowParttens") is not None:
            self.SlowParttens = []
            for item in params.get("SlowParttens"):
                obj = SlowPartten()
                obj._deserialize(item)
                self.SlowParttens.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSlowQuerysRequest(AbstractModel):
    """DescribeSlowQuerys请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cmgo-p8vnipr5，与云数据库控制台页面中显示的实例ID相同，可使用查询实例列表接口获取，其值为输出参数中字段 InstanceId 的值
        :type InstanceId: str
        :param StartTime: 开始时间
        :type StartTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        :param QueryMaxTime: 最大时间
        :type QueryMaxTime: int
        :param Offset: 偏移
        :type Offset: int
        :param Limit: 返回条数
        :type Limit: int
        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.QueryMaxTime = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.QueryMaxTime = params.get("QueryMaxTime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeSlowQuerysResponse(AbstractModel):
    """DescribeSlowQuerys返回参数结构体

    """

    def __init__(self):
        """
        :param Count: 记录数量
        :type Count: int
        :param SlowQuerys: 慢查询列表
        :type SlowQuerys: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Count = None
        self.SlowQuerys = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        self.SlowQuerys = params.get("SlowQuerys")
        self.RequestId = params.get("RequestId")


class DescribeTasksRequest(AbstractModel):
    """DescribeTasks请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cmgo-p8vnipr5，与云数据库控制台页面中显示的实例ID相同，可使用查询实例列表接口获取，其值为输出参数中字段 InstanceId 的值
        :type InstanceId: int
        :param InstanceName: 实例名字
        :type InstanceName: str
        :param Limit: 单页显示数量
        :type Limit: int
        :param Offset: 页码
        :type Offset: int
        :param ProjectIds: 项目ID过滤
        :type ProjectIds: list of int
        :param Fcodes: 任务类型过滤
        :type Fcodes: list of str
        :param BeginTime: 开始时间
        :type BeginTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        :param Status: 任务状态过滤
        :type Status: list of int
        """
        self.InstanceId = None
        self.InstanceName = None
        self.Limit = None
        self.Offset = None
        self.ProjectIds = None
        self.Fcodes = None
        self.BeginTime = None
        self.EndTime = None
        self.Status = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.ProjectIds = params.get("ProjectIds")
        self.Fcodes = params.get("Fcodes")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.Status = params.get("Status")


class DescribeTasksResponse(AbstractModel):
    """DescribeTasks返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 数量
        :type TotalCount: int
        :param Tasks: 任务列表
        :type Tasks: list of TaskInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Tasks = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Tasks") is not None:
            self.Tasks = []
            for item in params.get("Tasks"):
                obj = TaskInfo()
                obj._deserialize(item)
                self.Tasks.append(obj)
        self.RequestId = params.get("RequestId")


class FormalDBInstanceRequest(AbstractModel):
    """FormalDBInstance请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cmgo-p8vnipr5，与云数据库控制台页面中显示的实例ID相同，可使用查询实例列表接口获取，其值为输出参数中字段 InstanceId 的值
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class FormalDBInstanceResponse(AbstractModel):
    """FormalDBInstance返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class InitDBInstanceRequest(AbstractModel):
    """InitDBInstance请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cmgo-p8vnipr5，与云数据库控制台页面中显示的实例ID相同，可使用查询实例列表接口获取，其值为输出参数中字段 InstanceId 的值
        :type InstanceId: str
        :param Password: 实例新的密码，密码规则：8-64个字符，至少包含字母、数字、字符（支持的字符：!@#$%^*()）中的两种
        :type Password: str
        """
        self.InstanceId = None
        self.Password = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Password = params.get("Password")


class InitDBInstanceResponse(AbstractModel):
    """InitDBInstance返回参数结构体

    """

    def __init__(self):
        """
        :param AsyncRequestId: 异步任务的请求ID，可使用此ID查询异步任务的执行结果
        :type AsyncRequestId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class InquiryPriceCreateDBInstancesRequest(AbstractModel):
    """InquiryPriceCreateDBInstances请求参数结构体

    """

    def __init__(self):
        """
        :param Machine: 实例类型，GIO：高IO版；TGIO：高IO万兆
        :type Machine: str
        :param InstanceRole: 实例类型，默认为 MASTER，支持值包括：MASTER-表示主实例，DR-表示灾备实例，RO-表示只读实例
        :type InstanceRole: str
        :param GoodsNum: 购买商品数量
        :type GoodsNum: int
        :param Zone: 可用区信息
        :type Zone: str
        :param InstanceChargeType: 实例计费类型，PREPAID：预付费，即包年包月；POSTPAID_BY_HOUR：按小时后付费。
默认值：PREPAID
        :type InstanceChargeType: str
        :param InstanceType: 实例类型，REPLSET：副本集集群；SHARD：分片集群；DYNAMODB：DYNAMODB集群。默认值：REPLSET
        :type InstanceType: str
        :param ReplicateSetNum: 副本集个数，副本集模式下，该参数必须为1；分片模式下，该参数允许范围可以通过可售卖规格获取
        :type ReplicateSetNum: int
        :param SecondaryNum: 每个副本集内从节点个数，目前只支持从节点数为2
        :type SecondaryNum: int
        :param MongoVersion: MongoDB引擎版本，值包括：3.2wt、3.2rocks和3.6wt，请使用[查询可创建规格（支持可用区、配置自定义）](https://cloud.tencent.com/document/api/253/6109)接口获取可创建的实例版本
        :type MongoVersion: str
        :param Memory: 实例内存大小，单位：GB，请使用[查询可创建规格（支持可用区、配置自定义）](https://cloud.tencent.com/document/api/253/6109)接口获取可创建的内存规格
        :type Memory: int
        :param Volume: 实例硬盘大小，单位：GB，请使用[查询可创建规格（支持可用区、配置自定义）](https://cloud.tencent.com/document/api/253/6109)接口获取可创建的硬盘范围
        :type Volume: int
        """
        self.Machine = None
        self.InstanceRole = None
        self.GoodsNum = None
        self.Zone = None
        self.InstanceChargeType = None
        self.InstanceType = None
        self.ReplicateSetNum = None
        self.SecondaryNum = None
        self.MongoVersion = None
        self.Memory = None
        self.Volume = None


    def _deserialize(self, params):
        self.Machine = params.get("Machine")
        self.InstanceRole = params.get("InstanceRole")
        self.GoodsNum = params.get("GoodsNum")
        self.Zone = params.get("Zone")
        self.InstanceChargeType = params.get("InstanceChargeType")
        self.InstanceType = params.get("InstanceType")
        self.ReplicateSetNum = params.get("ReplicateSetNum")
        self.SecondaryNum = params.get("SecondaryNum")
        self.MongoVersion = params.get("MongoVersion")
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")


class InquiryPriceCreateDBInstancesResponse(AbstractModel):
    """InquiryPriceCreateDBInstances返回参数结构体

    """

    def __init__(self):
        """
        :param OriginalPrice: 原价
        :type OriginalPrice: float
        :param DiscountPrice: 折扣价
        :type DiscountPrice: float
        :param ChargeUnit: 价格单位
        :type ChargeUnit: str
        :param PriceCurrency: 折扣
        :type PriceCurrency: str
        :param ChargeStandard: 按量计费阶梯价格
        :type ChargeStandard: list of ChargeItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.OriginalPrice = None
        self.DiscountPrice = None
        self.ChargeUnit = None
        self.PriceCurrency = None
        self.ChargeStandard = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OriginalPrice = params.get("OriginalPrice")
        self.DiscountPrice = params.get("DiscountPrice")
        self.ChargeUnit = params.get("ChargeUnit")
        self.PriceCurrency = params.get("PriceCurrency")
        if params.get("ChargeStandard") is not None:
            self.ChargeStandard = []
            for item in params.get("ChargeStandard"):
                obj = ChargeItem()
                obj._deserialize(item)
                self.ChargeStandard.append(obj)
        self.RequestId = params.get("RequestId")


class InquiryPriceUpgradeDBInstancesRequest(AbstractModel):
    """InquiryPriceUpgradeDBInstances请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cdb-c1nl9rpv或者cdbro-c1nl9rpv。与云数据库控制台页面中显示的实例ID相同，可使用查询实例列表 接口获取，其值为输出参数中字段 InstanceId 的值
        :type InstanceId: str
        :param Memory: 升级后的内存大小，单位：MB，为保证传入 Memory 值有效，请使用查询可创建规格（支持可用区、配置自定义）接口获取可升级的内存规格
        :type Memory: int
        :param Volume: 升级后的硬盘大小，单位：GB，为保证传入 Volume 值有效，请使用查询可创建规格（支持可用区、配置自定义）接口获取可升级的硬盘范围
        :type Volume: int
        """
        self.InstanceId = None
        self.Memory = None
        self.Volume = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")


class InquiryPriceUpgradeDBInstancesResponse(AbstractModel):
    """InquiryPriceUpgradeDBInstances返回参数结构体

    """

    def __init__(self):
        """
        :param OriginalPrice: 原价
        :type OriginalPrice: float
        :param DiscountPrice: 折扣价
        :type DiscountPrice: float
        :param ChargeUnit: 价格单位
        :type ChargeUnit: str
        :param PriceCurrency: 折扣
        :type PriceCurrency: str
        :param ChargeStandard: 按量计费阶梯价格
        :type ChargeStandard: list of ChargeItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.OriginalPrice = None
        self.DiscountPrice = None
        self.ChargeUnit = None
        self.PriceCurrency = None
        self.ChargeStandard = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OriginalPrice = params.get("OriginalPrice")
        self.DiscountPrice = params.get("DiscountPrice")
        self.ChargeUnit = params.get("ChargeUnit")
        self.PriceCurrency = params.get("PriceCurrency")
        if params.get("ChargeStandard") is not None:
            self.ChargeStandard = []
            for item in params.get("ChargeStandard"):
                obj = ChargeItem()
                obj._deserialize(item)
                self.ChargeStandard.append(obj)
        self.RequestId = params.get("RequestId")


class InstanceInfo(AbstractModel):
    """实例详细信息

    """

    def __init__(self):
        """
        :param ZoneId: 可用区信息
        :type ZoneId: str
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param Volume: 硬盘容量，单位为G
        :type Volume: int
        :param VpcId: 私有网络ID，基础网络下为0
        :type VpcId: str
        :param SubnetId: 子网ID，基础网络下为0
        :type SubnetId: str
        :param InstanceType: 实例类型，REPLSET：副本集集群；SHARD：分片集群；DYNAMODB：DYNAMODB集群。
        :type InstanceType: str
        :param Region: 地域信息
        :type Region: str
        :param InstanceName: 实例名称
        :type InstanceName: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param DeadlineTime: 到期时间
        :type DeadlineTime: str
        :param Vip: 实例IP
        :type Vip: str
        :param Vport: 端口号
        :type Vport: str
        :param InstanceChargeType: 付费类型，PREPAID：预付费，即包年包月；POSTPAID_BY_HOUR：按小时后付费。
        :type InstanceChargeType: str
        :param Memory: 内存大小，单位为G
        :type Memory: int
        :param InstanceRole: 实例类型，默认为 MASTER，支持值包括：MASTER-表示主实例，TEMP-表示临时实例，DR-表示灾备实例，RO-表示只读实例
        :type InstanceRole: str
        :param OplogSize: oplog大小，单位为G
        :type OplogSize: int
        :param MongoVersion: MongoDB引擎版本，值包括：3.2wt、3.2rocks和3.6wt，请使用[查询可创建规格（支持可用区、配置自定义）](https://cloud.tencent.com/document/api/253/6109)接口获取可创建的实例版本
        :type MongoVersion: str
        :param Machine: 实例类型，GIO：高IO版；TGIO：高IO万兆
        :type Machine: str
        :param Status: 实例状态，0-待初始化；1-流程处理中；2-运行中；-2-已隔离。
        :type Status: int
        :param Replicates: 副本集信息
        :type Replicates: list of ReplicateInfo
        :param InstanceFlow: 实例当前运行状态信息
        :type InstanceFlow: str
        :param MasterInfo: 主实例信息
        :type MasterInfo: str
        :param TempInstanceId: 临时实例信息
        :type TempInstanceId: str
        :param ROInstanceIds: 只读实例信息
        :type ROInstanceIds: list of str
        :param DRInstanceIds: 灾备实例信息
        :type DRInstanceIds: list of str
        """
        self.ZoneId = None
        self.InstanceId = None
        self.Volume = None
        self.VpcId = None
        self.SubnetId = None
        self.InstanceType = None
        self.Region = None
        self.InstanceName = None
        self.CreateTime = None
        self.DeadlineTime = None
        self.Vip = None
        self.Vport = None
        self.InstanceChargeType = None
        self.Memory = None
        self.InstanceRole = None
        self.OplogSize = None
        self.MongoVersion = None
        self.Machine = None
        self.Status = None
        self.Replicates = None
        self.InstanceFlow = None
        self.MasterInfo = None
        self.TempInstanceId = None
        self.ROInstanceIds = None
        self.DRInstanceIds = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.InstanceId = params.get("InstanceId")
        self.Volume = params.get("Volume")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.InstanceType = params.get("InstanceType")
        self.Region = params.get("Region")
        self.InstanceName = params.get("InstanceName")
        self.CreateTime = params.get("CreateTime")
        self.DeadlineTime = params.get("DeadlineTime")
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        self.InstanceChargeType = params.get("InstanceChargeType")
        self.Memory = params.get("Memory")
        self.InstanceRole = params.get("InstanceRole")
        self.OplogSize = params.get("OplogSize")
        self.MongoVersion = params.get("MongoVersion")
        self.Machine = params.get("Machine")
        self.Status = params.get("Status")
        if params.get("Replicates") is not None:
            self.Replicates = []
            for item in params.get("Replicates"):
                obj = ReplicateInfo()
                obj._deserialize(item)
                self.Replicates.append(obj)
        self.InstanceFlow = params.get("InstanceFlow")
        self.MasterInfo = params.get("MasterInfo")
        self.TempInstanceId = params.get("TempInstanceId")
        self.ROInstanceIds = params.get("ROInstanceIds")
        self.DRInstanceIds = params.get("DRInstanceIds")


class IsolateDBInstanceRequest(AbstractModel):
    """IsolateDBInstance请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIds: 实例ID，格式如：cmgo-p8vnipr5，与云数据库控制台页面中显示的实例ID相同，可使用[查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值
        :type InstanceIds: list of str
        """
        self.InstanceIds = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")


class IsolateDBInstanceResponse(AbstractModel):
    """IsolateDBInstance返回参数结构体

    """

    def __init__(self):
        """
        :param AsyncRequestIds: 异步任务的请求ID，可使用此ID查询异步任务的执行结果
        :type AsyncRequestIds: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AsyncRequestIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestIds = params.get("AsyncRequestIds")
        self.RequestId = params.get("RequestId")


class ManualCreateBackupRequest(AbstractModel):
    """ManualCreateBackup请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cmgo-p8vnipr5，与云数据库控制台页面中显示的实例ID相同，可使用查询实例列表接口获取，其值为输出参数中字段 InstanceId 的值
        :type InstanceId: str
        :param BackupName: 手动备份名字
        :type BackupName: str
        :param BackupRemark: 备份说明
        :type BackupRemark: str
        """
        self.InstanceId = None
        self.BackupName = None
        self.BackupRemark = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.BackupName = params.get("BackupName")
        self.BackupRemark = params.get("BackupRemark")


class ManualCreateBackupResponse(AbstractModel):
    """ManualCreateBackup返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 任务Id
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class ModifyAccountAuthRequest(AbstractModel):
    """ModifyAccountAuth请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cmgo-p8vnipr5，与云数据库控制台页面中显示的实例ID相同，可使用查询实例列表接口获取，其值为输出参数中字段 InstanceId 的值
        :type InstanceId: str
        :param Account: 账户名字
        :type Account: str
        :param AuthRoles: 权限列表
        :type AuthRoles: list of Auth
        """
        self.InstanceId = None
        self.Account = None
        self.AuthRoles = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Account = params.get("Account")
        if params.get("AuthRoles") is not None:
            self.AuthRoles = []
            for item in params.get("AuthRoles"):
                obj = Auth()
                obj._deserialize(item)
                self.AuthRoles.append(obj)


class ModifyAccountAuthResponse(AbstractModel):
    """ModifyAccountAuth返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 任务列表
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class ModifyAccountPasswordRequest(AbstractModel):
    """ModifyAccountPassword请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cmgo-p8vnipr5，与云数据库控制台页面中显示的实例ID相同，可使用查询实例列表接口获取，其值为输出参数中字段 InstanceId 的值
        :type InstanceId: str
        :param Account: 账号名字
        :type Account: str
        :param OldPassword: 旧密码
        :type OldPassword: str
        :param Password: 新密码
        :type Password: str
        :param OpType: 操作类型  init,forget,reset
        :type OpType: str
        """
        self.InstanceId = None
        self.Account = None
        self.OldPassword = None
        self.Password = None
        self.OpType = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Account = params.get("Account")
        self.OldPassword = params.get("OldPassword")
        self.Password = params.get("Password")
        self.OpType = params.get("OpType")


class ModifyAccountPasswordResponse(AbstractModel):
    """ModifyAccountPassword返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 任务Id
        :type FlowId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class ModifyAutoRenewFlagRequest(AbstractModel):
    """ModifyAutoRenewFlag请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIds: 实例的ID，格式如：cmgo-p8vnipr5，与云数据库控制台页面中显示的实例ID相同
        :type InstanceIds: list of str
        :param AutoRenew: 自动续费的标记：0-不自动续费，1-自动续费，2-不续费
        :type AutoRenew: int
        """
        self.InstanceIds = None
        self.AutoRenew = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.AutoRenew = params.get("AutoRenew")


class ModifyAutoRenewFlagResponse(AbstractModel):
    """ModifyAutoRenewFlag返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDBInstanceFormalRequest(AbstractModel):
    """ModifyDBInstanceFormal请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cmgo-p8vnipr5，与云数据库控制台页面中显示的实例ID相同，可使用查询实例列表接口获取，其值为输出参数中字段 InstanceId 的值
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class ModifyDBInstanceFormalResponse(AbstractModel):
    """ModifyDBInstanceFormal返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDBInstanceNameRequest(AbstractModel):
    """ModifyDBInstanceName请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cmgo-p8vnipr5，与云数据库控制台页面中显示的实例ID相同，可使用查询实例列表接口获取，其值为输出参数中字段 InstanceId 的值
        :type InstanceId: str
        :param InstanceName: 实例新的名字
        :type InstanceName: str
        """
        self.InstanceId = None
        self.InstanceName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")


class ModifyDBInstanceNameResponse(AbstractModel):
    """ModifyDBInstanceName返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDBInstanceProjectRequest(AbstractModel):
    """ModifyDBInstanceProject请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIds: 实例Id列表
        :type InstanceIds: list of int
        :param NewProjectId: 新的项目Id
        :type NewProjectId: int
        """
        self.InstanceIds = None
        self.NewProjectId = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.NewProjectId = params.get("NewProjectId")


class ModifyDBInstanceProjectResponse(AbstractModel):
    """ModifyDBInstanceProject返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyReadonlyToNormalRequest(AbstractModel):
    """ModifyReadonlyToNormal请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cmgo-p8vnipr5，与云数据库控制台页面中显示的实例ID相同，可使用查询实例列表接口获取，其值为输出参数中字段 InstanceId 的值
        :type InstanceId: str
        :param FaterInstanceId: 父实例Id
        :type FaterInstanceId: str
        """
        self.InstanceId = None
        self.FaterInstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.FaterInstanceId = params.get("FaterInstanceId")


class ModifyReadonlyToNormalResponse(AbstractModel):
    """ModifyReadonlyToNormal返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 任务Id
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class Oplog(AbstractModel):
    """mongodb的Oplog描述

    """

    def __init__(self):
        """
        :param RsName: 集群节点名
        :type RsName: str
        :param LogSize: 日志大小
        :type LogSize: int
        :param TimeDiffHours: Oplog保存时间
        :type TimeDiffHours: int
        """
        self.RsName = None
        self.LogSize = None
        self.TimeDiffHours = None


    def _deserialize(self, params):
        self.RsName = params.get("RsName")
        self.LogSize = params.get("LogSize")
        self.TimeDiffHours = params.get("TimeDiffHours")


class RecycleDBInstanceRequest(AbstractModel):
    """RecycleDBInstance请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cmgo-p8vnipr5，与云数据库控制台页面中显示的实例ID相同，可使用查询实例列表接口获取，其值为输出参数中字段 InstanceId 的值
        :type InstanceId: str
        :param ZoneId: 区域Id
        :type ZoneId: int
        """
        self.InstanceId = None
        self.ZoneId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ZoneId = params.get("ZoneId")


class RecycleDBInstanceResponse(AbstractModel):
    """RecycleDBInstance返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 任务Id
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class RenewDBInstancesRequest(AbstractModel):
    """RenewDBInstances请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIds: 待续费数据库实例的ID，格式如：cmgo-p8vnipr5，与云数据库控制台页面中显示的实例ID相同
        :type InstanceIds: list of str
        :param Period: 续费时长，单位：月， 取值范围 [1,2,3,4,5,6,7,8,9,10,11,12,24,36]
        :type Period: int
        """
        self.InstanceIds = None
        self.Period = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.Period = params.get("Period")


class RenewDBInstancesResponse(AbstractModel):
    """RenewDBInstances返回参数结构体

    """

    def __init__(self):
        """
        :param DealIds: 短订单ID，用于调用云API相关接口，如[获取订单信息](https://cloud.tencent.com/document/api/403/4392)
        :type DealIds: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DealIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealIds = params.get("DealIds")
        self.RequestId = params.get("RequestId")


class ReplaceDBInstanceRequest(AbstractModel):
    """ReplaceDBInstance请求参数结构体

    """

    def __init__(self):
        """
        :param OldInstanceId: 旧的实例Id
        :type OldInstanceId: str
        :param NewInstanceId: 新的实例Id
        :type NewInstanceId: str
        """
        self.OldInstanceId = None
        self.NewInstanceId = None


    def _deserialize(self, params):
        self.OldInstanceId = params.get("OldInstanceId")
        self.NewInstanceId = params.get("NewInstanceId")


class ReplaceDBInstanceResponse(AbstractModel):
    """ReplaceDBInstance返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 任务Id
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class ReplicateInfo(AbstractModel):
    """副本集信息

    """

    def __init__(self):
        """
        :param MonitorDimension: 监控维度
        :type MonitorDimension: str
        :param ReplicasetId: 副本集ID
        :type ReplicasetId: str
        :param Memory: 内存，单位为G
        :type Memory: int
        :param Volume: 磁盘，单位为G
        :type Volume: int
        :param OplogSize: Oplog大小，单位为G
        :type OplogSize: int
        """
        self.MonitorDimension = None
        self.ReplicasetId = None
        self.Memory = None
        self.Volume = None
        self.OplogSize = None


    def _deserialize(self, params):
        self.MonitorDimension = params.get("MonitorDimension")
        self.ReplicasetId = params.get("ReplicasetId")
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        self.OplogSize = params.get("OplogSize")


class ResizeDBInstanceOplopRequest(AbstractModel):
    """ResizeDBInstanceOplop请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cmgo-p8vnipr5，与云数据库控制台页面中显示的实例ID相同，可使用查询实例列表接口获取，其值为输出参数中字段 InstanceId 的值
        :type InstanceId: str
        :param ShardId: 实例中单个点Id
        :type ShardId: str
        :param OplogSize: 调整后Oplog大小
        :type OplogSize: int
        """
        self.InstanceId = None
        self.ShardId = None
        self.OplogSize = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.ShardId = params.get("ShardId")
        self.OplogSize = params.get("OplogSize")


class ResizeDBInstanceOplopResponse(AbstractModel):
    """ResizeDBInstanceOplop返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 任务Id
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class RestartDBInstancesRequest(AbstractModel):
    """RestartDBInstances请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIds: 实例数组
        :type InstanceIds: list of str
        :param RestartType: 重启方式:1重启mognos, 2重启mongod, 3mognos和mongod都重启
        :type RestartType: int
        """
        self.InstanceIds = None
        self.RestartType = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.RestartType = params.get("RestartType")


class RestartDBInstancesResponse(AbstractModel):
    """RestartDBInstances返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RestoreDBInstanceRequest(AbstractModel):
    """RestoreDBInstance请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cmgo-p8vnipr5，与云数据库控制台页面中显示的实例ID相同，可使用查询实例列表接口获取，其值为输出参数中字段 InstanceId 的值
        :type InstanceId: str
        :param RestoreTime: 要回档的时间点
        :type RestoreTime: str
        """
        self.InstanceId = None
        self.RestoreTime = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.RestoreTime = params.get("RestoreTime")


class RestoreDBInstanceResponse(AbstractModel):
    """RestoreDBInstance返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 任务Id
        :type FlowId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class RestoreDbInfo(AbstractModel):
    """回档数据库信息

    """

    def __init__(self):
        """
        :param OldDbName: 回档旧的数据库名
        :type OldDbName: str
        :param NewDbName: 回档目标数据库名
        :type NewDbName: str
        :param Tables: 回档表List
        :type Tables: list of RestoreTableInfo
        """
        self.OldDbName = None
        self.NewDbName = None
        self.Tables = None


    def _deserialize(self, params):
        self.OldDbName = params.get("OldDbName")
        self.NewDbName = params.get("NewDbName")
        if params.get("Tables") is not None:
            self.Tables = []
            for item in params.get("Tables"):
                obj = RestoreTableInfo()
                obj._deserialize(item)
                self.Tables.append(obj)


class RestoreTableInfo(AbstractModel):
    """回档表信息

    """

    def __init__(self):
        """
        :param OldTableName: 旧的表名
        :type OldTableName: str
        :param NewTableName: 新的表名
        :type NewTableName: str
        """
        self.OldTableName = None
        self.NewTableName = None


    def _deserialize(self, params):
        self.OldTableName = params.get("OldTableName")
        self.NewTableName = params.get("NewTableName")


class RestoreTablesRequest(AbstractModel):
    """RestoreTables请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cmgo-p8vnipr5，与云数据库控制台页面中显示的实例ID相同，可使用查询实例列表接口获取，其值为输出参数中字段 InstanceId 的值
        :type InstanceId: str
        :param RestoreTime: 回档时间点
        :type RestoreTime: str
        :param Targets: 回档数据库表信息
        :type Targets: list of RestoreDbInfo
        """
        self.InstanceId = None
        self.RestoreTime = None
        self.Targets = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.RestoreTime = params.get("RestoreTime")
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = RestoreDbInfo()
                obj._deserialize(item)
                self.Targets.append(obj)


class RestoreTablesResponse(AbstractModel):
    """RestoreTables返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 任务Id
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class ScanAppInfo(AbstractModel):
    """app的基本信息对象

    """

    def __init__(self):
        """
        :param DataType: APP数据类型: 1-App URL
        :type DataType: int
        :param Data: APP数据,DataType=1时填写 App包的下载地址
        :type Data: str
        :param Md5: APP包的MD5值,DataType=1时必填,用于文件校验
        :type Md5: str
        :param Size: APP包大小(单位:字节),DataType=1时必填,用于文件校验
        :type Size: int
        :param CallbackUrl: 任务处理完成后的反向通知回调地址,通知为GET请求,请求URL: callbackUrl+"?ItemId=xxx&TaskStatus=1"; ItemId为应用加固接口返回的任务ID; TaskStatus为任务状态: 1-已完成,2-处理中,3-处理出错,4-处理超时; 对于应用加固,接收到通知后如果TaskStatus为1则可通过对应的查询接口查询加固结果
        :type CallbackUrl: str
        """
        self.DataType = None
        self.Data = None
        self.Md5 = None
        self.Size = None
        self.CallbackUrl = None


    def _deserialize(self, params):
        self.DataType = params.get("DataType")
        self.Data = params.get("Data")
        self.Md5 = params.get("Md5")
        self.Size = params.get("Size")
        self.CallbackUrl = params.get("CallbackUrl")


class SlowPartten(AbstractModel):
    """慢查询模式单条信息

    """

    def __init__(self):
        """
        :param QueryDetail: 查询详情
        :type QueryDetail: str
        :param AvgTime: 平均时间
        :type AvgTime: int
        :param Count: 调用次数
        :type Count: int
        :param MaxTime: 最大时间
        :type MaxTime: int
        :param Partten: 模式
        :type Partten: str
        """
        self.QueryDetail = None
        self.AvgTime = None
        self.Count = None
        self.MaxTime = None
        self.Partten = None


    def _deserialize(self, params):
        self.QueryDetail = params.get("QueryDetail")
        self.AvgTime = params.get("AvgTime")
        self.Count = params.get("Count")
        self.MaxTime = params.get("MaxTime")
        self.Partten = params.get("Partten")


class TaskInfo(AbstractModel):
    """任务信息

    """

    def __init__(self):
        """
        :param FlowID: 任务ID
        :type FlowID: int
        :param StartTime: 开始时间
        :type StartTime: str
        :param Fcode: 任务类型
        :type Fcode: int
        :param InstanceName: 实例名称
        :type InstanceName: str
        :param InstanceId: 实例Id
        :type InstanceId: int
        :param AppId: 应用Id
        :type AppId: int
        :param ProjectId: 项目Id
        :type ProjectId: int
        :param Result: 处理结果
        :type Result: int
        :param Progress: 进度
        :type Progress: int
        :param FlowDesc: 流程描述
        :type FlowDesc: str
        """
        self.FlowID = None
        self.StartTime = None
        self.Fcode = None
        self.InstanceName = None
        self.InstanceId = None
        self.AppId = None
        self.ProjectId = None
        self.Result = None
        self.Progress = None
        self.FlowDesc = None


    def _deserialize(self, params):
        self.FlowID = params.get("FlowID")
        self.StartTime = params.get("StartTime")
        self.Fcode = params.get("Fcode")
        self.InstanceName = params.get("InstanceName")
        self.InstanceId = params.get("InstanceId")
        self.AppId = params.get("AppId")
        self.ProjectId = params.get("ProjectId")
        self.Result = params.get("Result")
        self.Progress = params.get("Progress")
        self.FlowDesc = params.get("FlowDesc")


class TerminateDBInstanceRequest(AbstractModel):
    """TerminateDBInstance请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cmgo-p8vnipr5，与云数据库控制台页面中显示的实例ID相同，可使用查询实例列表接口获取，其值为输出参数中字段 InstanceId 的值
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class TerminateDBInstanceResponse(AbstractModel):
    """TerminateDBInstance返回参数结构体

    """

    def __init__(self):
        """
        :param FlowId: 任务Id
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class TerminateTempDBInstanceRequest(AbstractModel):
    """TerminateTempDBInstance请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class TerminateTempDBInstanceResponse(AbstractModel):
    """TerminateTempDBInstance返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpgradeDBInstanceHourRequest(AbstractModel):
    """UpgradeDBInstanceHour请求参数结构体

    """

    def __init__(self):
        """
        :param Memory: 内存
        :type Memory: int
        :param Volume: 磁盘
        :type Volume: int
        :param OplogSize: oplog大小，最少为磁盘的10%，最大为90%
        :type OplogSize: int
        :param InstanceId: 实例ID
        :type InstanceId: str
        """
        self.Memory = None
        self.Volume = None
        self.OplogSize = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        self.OplogSize = params.get("OplogSize")
        self.InstanceId = params.get("InstanceId")


class UpgradeDBInstanceHourResponse(AbstractModel):
    """UpgradeDBInstanceHour返回参数结构体

    """

    def __init__(self):
        """
        :param DealId: 短订单ID，用于调用云API相关接口，如获取订单信息
        :type DealId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DealId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealId = params.get("DealId")
        self.RequestId = params.get("RequestId")


class UpgradeDBInstanceRequest(AbstractModel):
    """UpgradeDBInstance请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID，格式如：cmgo-p8vnipr5。与云数据库控制台页面中显示的实例ID相同，可使用[查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口获取，其值为输出参数中字段 InstanceId 的值
        :type InstanceId: str
        :param Memory: 升级后的内存大小，单位：GB，为保证传入 Memory 值有效，请使用[查询可创建规格（支持可用区、配置自定义）](https://cloud.tencent.com/document/api/253/6109)接口获取可升级的内存规格
        :type Memory: int
        :param Volume: 升级后的硬盘大小，单位：GB，为保证传入 Volume 值有效，请使用[查询可创建规格（支持可用区、配置自定义）](https://cloud.tencent.com/document/api/253/6109)接口获取可升级的硬盘范围
        :type Volume: int
        :param OplogSize: 升级后oplog的大小，默认为磁盘空间的10%，允许设置的最小值为磁盘的10%，最大值为磁盘的90%
        :type OplogSize: int
        """
        self.InstanceId = None
        self.Memory = None
        self.Volume = None
        self.OplogSize = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Memory = params.get("Memory")
        self.Volume = params.get("Volume")
        self.OplogSize = params.get("OplogSize")


class UpgradeDBInstanceResponse(AbstractModel):
    """UpgradeDBInstance返回参数结构体

    """

    def __init__(self):
        """
        :param DealIds: 短订单ID，用于调用云API相关接口，如[获取订单信息](https://cloud.tencent.com/document/api/403/4392)
        :type DealIds: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DealIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealIds = params.get("DealIds")
        self.RequestId = params.get("RequestId")
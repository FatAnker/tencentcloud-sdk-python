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


class AdderrorRequest(AbstractModel):
    """Adderror请求参数结构体

    """

    def __init__(self):
        """
        :param UserType: asdf
        :type UserType: list of str datetime
        """
        self.UserType = None


    def _deserialize(self, params):
        self.UserType = params.get("UserType")


class AdderrorResponse(AbstractModel):
    """Adderror返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ClearRedisRequest(AbstractModel):
    """ClearRedis请求参数结构体

    """

    def __init__(self):
        """
        :param RedisId: 实例id
        :type RedisId: str
        :param Password: redis的实例密码
        :type Password: str
        """
        self.RedisId = None
        self.Password = None


    def _deserialize(self, params):
        self.RedisId = params.get("RedisId")
        self.Password = params.get("Password")


class ClearRedisResponse(AbstractModel):
    """ClearRedis返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务Id
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CreateRedisHourRequest(AbstractModel):
    """CreateRedisHour请求参数结构体

    """

    def __init__(self):
        """
        :param ZoneId: 实例所属的可用区id
        :type ZoneId: int
        :param TypeId: 实例类型：1 – 集群版，2 – 主从版，3-新一代主从版，4-ckv集群版
        :type TypeId: int
        :param MemSize: 实例容量，单位MB， 取值大小以 查询售卖规格接口返回的规格为准， 取值范围[data.types.minMemSize, data.types.maxMemSize]
        :type MemSize: int
        :param GoodsNum: 实例数量，单次购买实例数量以 查询售卖规格接口返回的规格为准， 取值范[data.types.minBuyNum, data.types.maxBuyNum]
        :type GoodsNum: int
        :param Period: 购买时长，单位：月，取值范围 [1,2,3,4,5,6,7,8,9,10,11,12,24,36]
        :type Period: int
        :param Password: 实例密码，密码规则：1.长度为8-16个字符；2:至少包含字母、数字和字符（!@#%^()）中的两种
        :type Password: str
        :param VpcId: 历史原因，仍保留该参数，推荐使用下面参数unVpcId。 私有网络ID，如果不传则默认选择基础网络。
        :type VpcId: list of int
        :param UnVpcId: 私有网络ID，如果不传则默认选择基础网络，请使用私有网络列表 查询 返回的unVpcId为准，如：vpc-kd7d06of
        :type UnVpcId: str
        :param SubnetId: 历史原因，仍保留该参数，推荐使用下面参数unSubnetId。私有网络下的子网ID，如果设置了 vpcId，则 subnetId 必填。
        :type SubnetId: int
        :param UnSubnetId: 基础网络下， subnetId无效； vpc子网下，取值以查询查询子网列表 返回的unSubnetId为准，如：subnet-3lzrkspo
        :type UnSubnetId: str
        :param ProjectId: 项目id，取值以用户账户>用户账户相关接口查询>项目列表返回的projectId为准
        :type ProjectId: int
        :param AutoRenewFlag: 自动续费表示。0 - 默认状态（手动续费）；1 - 自动续费；2 - 明确不自动续费
        :type AutoRenewFlag: int
        :param ZoneName: 安全组id数组
        :type ZoneName: str
        :param VPort: 用户自定义的端口 不填则默认为6379
        :type VPort: list of int
        :param SecurityGroupList: 实例所属区域名称，形如：ap-beijing-1、ap-shanghai-1、ap-guangzhou-1
        :type SecurityGroupList: list of int
        """
        self.ZoneId = None
        self.TypeId = None
        self.MemSize = None
        self.GoodsNum = None
        self.Period = None
        self.Password = None
        self.VpcId = None
        self.UnVpcId = None
        self.SubnetId = None
        self.UnSubnetId = None
        self.ProjectId = None
        self.AutoRenewFlag = None
        self.ZoneName = None
        self.VPort = None
        self.SecurityGroupList = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.TypeId = params.get("TypeId")
        self.MemSize = params.get("MemSize")
        self.GoodsNum = params.get("GoodsNum")
        self.Period = params.get("Period")
        self.Password = params.get("Password")
        self.VpcId = params.get("VpcId")
        self.UnVpcId = params.get("UnVpcId")
        self.SubnetId = params.get("SubnetId")
        self.UnSubnetId = params.get("UnSubnetId")
        self.ProjectId = params.get("ProjectId")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.ZoneName = params.get("ZoneName")
        self.VPort = params.get("VPort")
        self.SecurityGroupList = params.get("SecurityGroupList")


class CreateRedisHourResponse(AbstractModel):
    """CreateRedisHour返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID
        :type TaskId: int
        :param ResourceIds: 资源列表
        :type ResourceIds: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.ResourceIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.ResourceIds = params.get("ResourceIds")
        self.RequestId = params.get("RequestId")


class CreateRedisRequest(AbstractModel):
    """CreateRedis请求参数结构体

    """

    def __init__(self):
        """
        :param ZoneId: 实例所属的可用区id
        :type ZoneId: int
        :param TypeId: 实例类型：1 – 集群版，2 – 主从版，4，ckv集群版
        :type TypeId: int
        :param MemSize: 实例容量，单位MB， 取值大小以 查询售卖规格接口返回的规格为准， 取值范围[data.types.minMemSize, data.types.maxMemSize]
        :type MemSize: int
        :param GoodsNum: 实例数量，单次购买实例数量以 查询售卖规格接口返回的规格为准， 取值范[data.types.minBuyNum, data.types.maxBuyNum]
        :type GoodsNum: int
        :param Period: 购买时长，单位：月，取值范围 [1,2,3,4,5,6,7,8,9,10,11,12,24,36]
        :type Period: int
        :param Password: 实例密码，密码规则：1.长度为8-16个字符；2:至少包含字母、数字和字符（!@#%^()）中的两种
        :type Password: str
        :param VpcId: 历史原因，仍保留该参数，推荐使用下面参数unVpcId。 私有网络ID，如果不传则默认选择基础网络。
        :type VpcId: int
        :param UnVpcId: 私有网络ID，如果不传则默认选择基础网络，请使用私有网络列表 查询 返回的unVpcId为准，如：vpc-kd7d06of
        :type UnVpcId: str
        :param SubnetId: 历史原因，仍保留该参数，推荐使用下面参数unSubnetId。私有网络下的子网ID，如果设置了 vpcId，则 subnetId 必填。
        :type SubnetId: int
        :param UnSubnetId: 基础网络下， subnetId无效； vpc子网下，取值以查询查询子网列表 返回的unSubnetId为准，如：subnet-3lzrkspo
        :type UnSubnetId: str
        :param ProjectId: 项目id，取值以用户账户>用户账户相关接口查询>项目列表返回的projectId为准
        :type ProjectId: int
        :param AutoRenewFlag: 自动续费表示。0 - 默认状态（手动续费）；1 - 自动续费；2 - 明确不自动续费
        :type AutoRenewFlag: int
        :param SecurityGroupList: 安全组id数组
        :type SecurityGroupList: list of int
        :param VPort: 用户自定义的端口 不填则默认为6379
        :type VPort: int
        :param ZoneName: 实例所属区域名称，形如：ap-beijing-1、ap-shanghai-1、ap-guangzhou-1
        :type ZoneName: str
        """
        self.ZoneId = None
        self.TypeId = None
        self.MemSize = None
        self.GoodsNum = None
        self.Period = None
        self.Password = None
        self.VpcId = None
        self.UnVpcId = None
        self.SubnetId = None
        self.UnSubnetId = None
        self.ProjectId = None
        self.AutoRenewFlag = None
        self.SecurityGroupList = None
        self.VPort = None
        self.ZoneName = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.TypeId = params.get("TypeId")
        self.MemSize = params.get("MemSize")
        self.GoodsNum = params.get("GoodsNum")
        self.Period = params.get("Period")
        self.Password = params.get("Password")
        self.VpcId = params.get("VpcId")
        self.UnVpcId = params.get("UnVpcId")
        self.SubnetId = params.get("SubnetId")
        self.UnSubnetId = params.get("UnSubnetId")
        self.ProjectId = params.get("ProjectId")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.SecurityGroupList = params.get("SecurityGroupList")
        self.VPort = params.get("VPort")
        self.ZoneName = params.get("ZoneName")


class CreateRedisResponse(AbstractModel):
    """CreateRedis返回参数结构体

    """

    def __init__(self):
        """
        :param DealId: 交易的Id
        :type DealId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DealId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealId = params.get("DealId")
        self.RequestId = params.get("RequestId")


class DescribeRedisDealDetailRequest(AbstractModel):
    """DescribeRedisDealDetail请求参数结构体

    """

    def __init__(self):
        """
        :param DealIds: 交易ID列表
        :type DealIds: list of str
        """
        self.DealIds = None


    def _deserialize(self, params):
        self.DealIds = params.get("DealIds")


class DescribeRedisDealDetailResponse(AbstractModel):
    """DescribeRedisDealDetail返回参数结构体

    """

    def __init__(self):
        """
        :param DealDetails: 交易详情。
        :type DealDetails: :class:`tencentcloud.redis.v20180412.models.TradeDealDetails`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DealDetails = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DealDetails") is not None:
            self.DealDetails = TradeDealDetails()
            self.DealDetails._deserialize(params.get("DealDetails"))
        self.RequestId = params.get("RequestId")


class DescribeRedisProductRequest(AbstractModel):
    """DescribeRedisProduct请求参数结构体

    """

    def __init__(self):
        """
        :param ZoneIds: 可用区id组成的数组，数组下标从0开始, 若不传此参数将返回所有区域产品信息, 取值以查询售卖可用区返回为准
        :type ZoneIds: list of str
        :param TypeId: 实例类型：1 – 集群版，2 – 主从版, 3-新一代主从版，0 – 所有类型
        :type TypeId: int
        """
        self.ZoneIds = None
        self.TypeId = None


    def _deserialize(self, params):
        self.ZoneIds = params.get("ZoneIds")
        self.TypeId = params.get("TypeId")


class DescribeRedisProductResponse(AbstractModel):
    """DescribeRedisProduct返回参数结构体

    """

    def __init__(self):
        """
        :param Regions: 各地域的售卖规则
        :type Regions: :class:`tencentcloud.redis.v20180412.models.RegionConf`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Regions = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Regions") is not None:
            self.Regions = RegionConf()
            self.Regions._deserialize(params.get("Regions"))
        self.RequestId = params.get("RequestId")


class DescribeRedisRegionsRequest(AbstractModel):
    """DescribeRedisRegions请求参数结构体

    """


class DescribeRedisRegionsResponse(AbstractModel):
    """DescribeRedisRegions返回参数结构体

    """

    def __init__(self):
        """
        :param RegionSets: 地域列表。
        :type RegionSets: list of RedisRegion
        :param TotalCount: 地域数量。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RegionSets = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RegionSets") is not None:
            self.RegionSets = []
            for item in params.get("RegionSets"):
                obj = RedisRegion()
                obj._deserialize(item)
                self.RegionSets.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeRedisRequest(AbstractModel):
    """DescribeRedis请求参数结构体

    """

    def __init__(self):
        """
        :param Limit: 分页大小
        :type Limit: int
        :param Offset: 当前页码
        :type Offset: int
        :param RedisId: 实例Id
        :type RedisId: str
        :param RedisName: 实例名称
        :type RedisName: str
        :param OrderBy: 枚举范围redisId,projectId,createtime
        :type OrderBy: str
        :param OrderType: 1倒序，0顺序，默认倒序
        :type OrderType: int
        :param VpcIds: 历史原因，仍保留该参数，推荐使用下面参数unVpcIds。 私有网络ID数组，数组下标从0开始，如果不传则默认选择基础网络。
        :type VpcIds: list of int
        :param UnVpcIds: 私有网络ID数组，数组下标从0开始，如果不传则默认选择基础网络。请使用私有网络列表 查询返回的unVpcId为准，如：vpc-kd7d06of
        :type UnVpcIds: list of str
        :param SubnetIds: 历史原因，仍保留该参数，推荐使用下面参数unSubnetIds。私有网络下的子网ID数组，数组下标从0开始
        :type SubnetIds: list of int
        :param UnSubnetIds: 子网ID数组，数组下标从0开始。 vpc子网下，取值以查询查询子网列表 返回的unSubnetId为准，如：subnet-3lzrkspo
        :type UnSubnetIds: list of str
        :param ProjectIds: 项目ID 组成的数组，数组下标从0开始
        :type ProjectIds: list of str
        """
        self.Limit = None
        self.Offset = None
        self.RedisId = None
        self.RedisName = None
        self.OrderBy = None
        self.OrderType = None
        self.VpcIds = None
        self.UnVpcIds = None
        self.SubnetIds = None
        self.UnSubnetIds = None
        self.ProjectIds = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.RedisId = params.get("RedisId")
        self.RedisName = params.get("RedisName")
        self.OrderBy = params.get("OrderBy")
        self.OrderType = params.get("OrderType")
        self.VpcIds = params.get("VpcIds")
        self.UnVpcIds = params.get("UnVpcIds")
        self.SubnetIds = params.get("SubnetIds")
        self.UnSubnetIds = params.get("UnSubnetIds")
        self.ProjectIds = params.get("ProjectIds")


class DescribeRedisResponse(AbstractModel):
    """DescribeRedis返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 实例数
        :type TotalCount: int
        :param RedisSets: RedisSet数组
        :type RedisSets: list of RedisSet
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.RedisSets = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("RedisSets") is not None:
            self.RedisSets = []
            for item in params.get("RedisSets"):
                obj = RedisSet()
                obj._deserialize(item)
                self.RedisSets.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRegionsRequest(AbstractModel):
    """DescribeRegions请求参数结构体

    """


class DescribeRegionsResponse(AbstractModel):
    """DescribeRegions返回参数结构体

    """

    def __init__(self):
        """
        :param RegionSets: 地域列表。
        :type RegionSets: list of RedisRegion
        :param TotalCount: 地域数量。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RegionSets = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RegionSets") is not None:
            self.RegionSets = []
            for item in params.get("RegionSets"):
                obj = RedisRegion()
                obj._deserialize(item)
                self.RegionSets.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeTaskInfoRequest(AbstractModel):
    """DescribeTaskInfo请求参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID
        :type TaskId: int
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")


class DescribeTaskInfoResponse(AbstractModel):
    """DescribeTaskInfo返回参数结构体

    """

    def __init__(self):
        """
        :param Status: 任务状态0:待执行，1：执行中，2：成功，3：失败，-1 执行出错
        :type Status: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class ExportRedisBackupRequest(AbstractModel):
    """ExportRedisBackup请求参数结构体

    """

    def __init__(self):
        """
        :param RedisId: 待操作的实例ID，可通过 DescribeRedis 接口返回值中的 redisId 获取。
        :type RedisId: str
        :param BackupId: 备份ID，可通过 GetRedisBackupList 接口返回值中的 backupId 获取。
        :type BackupId: str
        """
        self.RedisId = None
        self.BackupId = None


    def _deserialize(self, params):
        self.RedisId = params.get("RedisId")
        self.BackupId = params.get("BackupId")


class ExportRedisBackupResponse(AbstractModel):
    """ExportRedisBackup返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class GetRedisBackupListRequest(AbstractModel):
    """GetRedisBackupList请求参数结构体

    """

    def __init__(self):
        """
        :param Limit: 分页大小。
        :type Limit: int
        :param Offset: 当前页码，默认为0。 查询接口中单次查询一般都有一个默认最大返回记录数，要遍历所有资源，需要使用 limit，offset进行分页查询；例如查询第110~149 这40条记录，则可以设置 offset=110 limit=40。
        :type Offset: int
        :param RedisId: 待操作的实例ID，可通过 DescribeRedis 接口返回值中的 redisId 获取。
        :type RedisId: str
        :param BeginTime: 开始时间，格式如：2017-02-08 16:46:34。查询实例在 [beginTime, endTime] 时间段内开始备份的备份列表。
        :type BeginTime: str
        :param EndTime: 结束时间，格式如：2017-02-08 19:09:26。查询实例在 [beginTime, endTime] 时间段内开始备份的备份列表。
        :type EndTime: str
        """
        self.Limit = None
        self.Offset = None
        self.RedisId = None
        self.BeginTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.RedisId = params.get("RedisId")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")


class GetRedisBackupListResponse(AbstractModel):
    """GetRedisBackupList返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 备份总数
        :type TotalCount: int
        :param RedisBackupSet: 实例的备份数组
        :type RedisBackupSet: list of RedisBackupSet
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.RedisBackupSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("RedisBackupSet") is not None:
            self.RedisBackupSet = []
            for item in params.get("RedisBackupSet"):
                obj = RedisBackupSet()
                obj._deserialize(item)
                self.RedisBackupSet.append(obj)
        self.RequestId = params.get("RequestId")


class GetRedisPerformanceRequest(AbstractModel):
    """GetRedisPerformance请求参数结构体

    """

    def __init__(self):
        """
        :param RedisIds: 实例ID列表
        :type RedisIds: list of str
        :param StartTime: 开始时间
        :type StartTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        """
        self.RedisIds = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.RedisIds = params.get("RedisIds")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class GetRedisPerformanceResponse(AbstractModel):
    """GetRedisPerformance返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class GetRedisSlowLogListRequest(AbstractModel):
    """GetRedisSlowLogList请求参数结构体

    """

    def __init__(self):
        """
        :param Limit: 页面大小
        :type Limit: int
        :param Offset: 当前页码
        :type Offset: int
        :param RedisId: 实例ID
        :type RedisId: str
        :param BeginTime: 开始时间
        :type BeginTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        :param QueryMaxTime: 慢查询阈值，单位微秒
        :type QueryMaxTime: int
        """
        self.Limit = None
        self.Offset = None
        self.RedisId = None
        self.BeginTime = None
        self.EndTime = None
        self.QueryMaxTime = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.RedisId = params.get("RedisId")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.QueryMaxTime = params.get("QueryMaxTime")


class GetRedisSlowLogListResponse(AbstractModel):
    """GetRedisSlowLogList返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 慢日志个数
        :type TotalCount: int
        :param SlowLogs: 慢查询日志数组
        :type SlowLogs: list of SlowlogDetail
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.SlowLogs = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("SlowLogs") is not None:
            self.SlowLogs = []
            for item in params.get("SlowLogs"):
                obj = SlowlogDetail()
                obj._deserialize(item)
                self.SlowLogs.append(obj)
        self.RequestId = params.get("RequestId")


class GetRedisTaskListRequest(AbstractModel):
    """GetRedisTaskList请求参数结构体

    """

    def __init__(self):
        """
        :param Limit: 分页大小
        :type Limit: int
        :param Offset: 当前页码，默认为0。 查询接口中单次查询一般都有一个默认最大返回记录数，要遍历所有资源，需要使用 limit，offset进行分页查询；例如查询第110~149 这40条记录，则可以设置 offset=110 limit=40。
        :type Offset: int
        :param RedisId: 实例ID, 可通过 DescribeRedis 接口返回值中的 redisId 获取，支持按照实例ID筛选任务。
        :type RedisId: str
        :param RedisName: 实例名称，可通过 DescribeRedis 接口返回值中的 redisName 获取，支持按照实例名称筛选任务。
        :type RedisName: str
        :param BeginTime: 开始时间，格式如：2017-02-08 16:46:34。 查询在 [beginTime, endTime] 时间段内提交的任务列表。
        :type BeginTime: str
        :param EndTime: 结束时间，格式如：2017-02-08 19:09:26。 查询在 [beginTime, endTime] 时间段内提交的任务列表。
        :type EndTime: str
        :param TaskStatus: 一个或者多个任务状态，n表示从0开始的数组下标。 支持按照任务状态筛选任务。 任务状态定义为
0：待执行;
1：执行中;
2：成功;
3：失败;
-1：执行出错
        :type TaskStatus: int
        :param TaskTypes: 一个或者多个任务类型，n表示从0开始的数组下标。 支持按照任务类型筛选。 任务类型定义为 :
'001'：task_newInstance：新建实例                                                                                                                                                                                                           
'002'：task_resizeInstance：升级实例的任务
'004'：task_cleanInstance：清空实例的任务；
'006'：task_deleteInstance：删除实例
'007'：task_setPassword'：设置密码
'008'：task_importRdb：导入Rdb的任务；
'009'：task_exportBackup：导出备份的任务；
'010'：task_restoreBackup：恢复实例的任务；
'011'：task_restoreStream：回档实例的任务（集群版实例可回档3天内任意时间点，但是，最近10分钟的数据不可回档）；
'012'：task_backupInstance：备份实例的任务；
        :type TaskTypes: list of int non-negative
        """
        self.Limit = None
        self.Offset = None
        self.RedisId = None
        self.RedisName = None
        self.BeginTime = None
        self.EndTime = None
        self.TaskStatus = None
        self.TaskTypes = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.RedisId = params.get("RedisId")
        self.RedisName = params.get("RedisName")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.TaskStatus = params.get("TaskStatus")
        self.TaskTypes = params.get("TaskTypes")


class GetRedisTaskListResponse(AbstractModel):
    """GetRedisTaskList返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 任务个数
        :type TotalCount: int
        :param RedisTaskSets: 任务详情数组
        :type RedisTaskSets: list of TaskInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.RedisTaskSets = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("RedisTaskSets") is not None:
            self.RedisTaskSets = []
            for item in params.get("RedisTaskSets"):
                obj = TaskInfo()
                obj._deserialize(item)
                self.RedisTaskSets.append(obj)
        self.RequestId = params.get("RequestId")


class GoodsDetail(AbstractModel):
    """商品详情

    """

    def __init__(self):
        """
        :param MemSize: 实例容量， 单位:MB
        :type MemSize: int
        :param TimeSpan: 购买时长， 单位以：timeUnit为准
        :type TimeSpan: int
        :param TimeUnit: 购买时长单位， m- 月， d - 天
        :type TimeUnit: int
        :param RedisIds: 关联的redisId列表
        :type RedisIds: list of str
        :param CurDeadline: 续费前，实例到期时间
        :type CurDeadline: str
        """
        self.MemSize = None
        self.TimeSpan = None
        self.TimeUnit = None
        self.RedisIds = None
        self.CurDeadline = None


    def _deserialize(self, params):
        self.MemSize = params.get("MemSize")
        self.TimeSpan = params.get("TimeSpan")
        self.TimeUnit = params.get("TimeUnit")
        self.RedisIds = params.get("RedisIds")
        self.CurDeadline = params.get("CurDeadline")


class InquiryRedisPriceRequest(AbstractModel):
    """InquiryRedisPrice请求参数结构体

    """

    def __init__(self):
        """
        :param ZoneId: 实例所属可用区, 取值以查询售卖可用区返回值为准
        :type ZoneId: int
        :param TypeId: 实例类型：1 – 集群版，2 – 主从版
        :type TypeId: int
        :param MemSize: 容量大小, 1024的整数倍，单位：MB， 大小限制以查询售卖规格接口返回为准
        :type MemSize: int
        :param GoodsNum: 实例数量，数量限制以查询售卖规格接口返回为准
        :type GoodsNum: int
        :param Period: 购买或续费时长, 单位：月， 取值范围 [1,2,3,4,5,6,7,8,9,10,11,12,24,36]
        :type Period: int
        :param BillingMode: 计费模式：0-按量计费，1-包年包月
        :type BillingMode: int
        """
        self.ZoneId = None
        self.TypeId = None
        self.MemSize = None
        self.GoodsNum = None
        self.Period = None
        self.BillingMode = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.TypeId = params.get("TypeId")
        self.MemSize = params.get("MemSize")
        self.GoodsNum = params.get("GoodsNum")
        self.Period = params.get("Period")
        self.BillingMode = params.get("BillingMode")


class InquiryRedisPriceResponse(AbstractModel):
    """InquiryRedisPrice返回参数结构体

    """

    def __init__(self):
        """
        :param Price: 购买或者续费实例的总费用，单位：分。
        :type Price: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Price = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Price = params.get("Price")
        self.RequestId = params.get("RequestId")


class IsolateRedisInstanceRequest(AbstractModel):
    """IsolateRedisInstance请求参数结构体

    """

    def __init__(self):
        """
        :param RedisId: 实例
        :type RedisId: str
        """
        self.RedisId = None


    def _deserialize(self, params):
        self.RedisId = params.get("RedisId")


class IsolateRedisInstanceResponse(AbstractModel):
    """IsolateRedisInstance返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ManualBackupInstanceRequest(AbstractModel):
    """ManualBackupInstance请求参数结构体

    """

    def __init__(self):
        """
        :param RedisId: 待操作的实例ID，可通过 DescribeRedis 接口返回值中的 redisId 获取。
        :type RedisId: str
        :param Remark: 备份的备注信息
        :type Remark: str
        """
        self.RedisId = None
        self.Remark = None


    def _deserialize(self, params):
        self.RedisId = params.get("RedisId")
        self.Remark = params.get("Remark")


class ManualBackupInstanceResponse(AbstractModel):
    """ManualBackupInstance返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ModifyRedisNameRequest(AbstractModel):
    """ModifyRedisName请求参数结构体

    """

    def __init__(self):
        """
        :param RedisId: 实例id
        :type RedisId: str
        :param RedisName: 实例名称
        :type RedisName: str
        """
        self.RedisId = None
        self.RedisName = None


    def _deserialize(self, params):
        self.RedisId = params.get("RedisId")
        self.RedisName = params.get("RedisName")


class ModifyRedisNameResponse(AbstractModel):
    """ModifyRedisName返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyRedisParamsRequest(AbstractModel):
    """ModifyRedisParams请求参数结构体

    """

    def __init__(self):
        """
        :param RedisId: 实例id
        :type RedisId: str
        :param ParamNameList: 参数名称列表
        :type ParamNameList: list of str
        :param ParamValueList: 参数值列表
        :type ParamValueList: list of str
        """
        self.RedisId = None
        self.ParamNameList = None
        self.ParamValueList = None


    def _deserialize(self, params):
        self.RedisId = params.get("RedisId")
        self.ParamNameList = params.get("ParamNameList")
        self.ParamValueList = params.get("ParamValueList")


class ModifyRedisParamsResponse(AbstractModel):
    """ModifyRedisParams返回参数结构体

    """

    def __init__(self):
        """
        :param Changed: true:设置成功；false:设置失败
        :type Changed: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Changed = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Changed = params.get("Changed")
        self.RequestId = params.get("RequestId")


class ModifyRedisProjectRequest(AbstractModel):
    """ModifyRedisProject请求参数结构体

    """

    def __init__(self):
        """
        :param RedisIds: 可通过DescribeRedis接口查询实例Id组成的数组，数组下标从0开始
        :type RedisIds: list of str
        :param ProjectId: 项目ID,取值以用户账户>用户账户相关接口查询>项目列表返回的projectId为准
        :type ProjectId: int
        """
        self.RedisIds = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.RedisIds = params.get("RedisIds")
        self.ProjectId = params.get("ProjectId")


class ModifyRedisProjectResponse(AbstractModel):
    """ModifyRedisProject返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RedisBackupSet(AbstractModel):
    """实例的备份数组

    """

    def __init__(self):
        """
        :param StartTime: 开始备份的时间
        :type StartTime: list of str
        :param BackupId: 备份ID
        :type BackupId: list of str
        :param BackupType: 备份类型。 manualBackupInstance：用户发起的手动备份； systemBackupInstance：凌晨系统发起的备份
        :type BackupType: list of str
        :param Status: 备份状态。  1:
        :type Status: int
        :param Remark: 备份的备注信息
        :type Remark: str
        :param Locked: 备份是否被锁定，0：未被锁定；1：已被锁定
        :type Locked: int
        """
        self.StartTime = None
        self.BackupId = None
        self.BackupType = None
        self.Status = None
        self.Remark = None
        self.Locked = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.BackupId = params.get("BackupId")
        self.BackupType = params.get("BackupType")
        self.Status = params.get("Status")
        self.Remark = params.get("Remark")
        self.Locked = params.get("Locked")


class RedisRegion(AbstractModel):
    """地域列表

    """

    def __init__(self):
        """
        :param RegionId: 地域id 1--广州 4--上海 5-- 香港 6--多伦多 7--上海金融 8--北京 9-- 新加坡 11--深圳金融 15--美西（硅谷）
        :type RegionId: int
        :param RegionCityNameEn: 地域英文名
        :type RegionCityNameEn: str
        :param RegionCityNameCn: 地域中文名
        :type RegionCityNameCn: str
        :param RegionCityNameLong: 地域完整信息
        :type RegionCityNameLong: str
        """
        self.RegionId = None
        self.RegionCityNameEn = None
        self.RegionCityNameCn = None
        self.RegionCityNameLong = None


    def _deserialize(self, params):
        self.RegionId = params.get("RegionId")
        self.RegionCityNameEn = params.get("RegionCityNameEn")
        self.RegionCityNameCn = params.get("RegionCityNameCn")
        self.RegionCityNameLong = params.get("RegionCityNameLong")


class RedisSet(AbstractModel):
    """redisSet列表

    """

    def __init__(self):
        """
        :param RedisName: 实例名称
        :type RedisName: str
        :param RedisId: 实例串号
        :type RedisId: str
        :param Appid: appid
        :type Appid: int
        :param ProjectId: 项目id
        :type ProjectId: int
        :param RegionId: 地域id 1--广州 4--上海 5-- 香港 6--多伦多 7--上海金融 8--北京 9-- 新加坡 11--深圳金融 15--美西（硅谷）
        :type RegionId: int
        :param ZoneId: 区域id
        :type ZoneId: int
        :param VpcId: vpc网络id，不推荐使用
        :type VpcId: int
        :param UnVpcId: vpc网络id，推荐使用
        :type UnVpcId: str
        :param SubnetId: vpc网络下子网id，不推荐使用
        :type SubnetId: int
        :param UnSubnetId: vpc网络下子网id，推荐使用
        :type UnSubnetId: str
        :param Status: 实例当前状态，0：待初始化；1：实例在流程中；2：实例运行中；-2：实例已隔离
        :type Status: int
        :param StatusDesc: 实例状态描述
        :type StatusDesc: str
        :param WanIp: 实例vip
        :type WanIp: str
        :param Port: 实例端口号
        :type Port: int
        :param Createtime: 实例创建时间
        :type Createtime: str
        :param Size: 实例容量大小，单位：MB
        :type Size: str
        :param SizeUsed: 实例当前已使用容量，单位：MB
        :type SizeUsed: int
        :param TypeId: 实例类型，1：集群版；2：主从版
        :type TypeId: int
        :param TypeIddesc: 实例类型描述
        :type TypeIddesc: str
        :param AutoRenewFlag: 实例是否设置自动续费标识，1：设置自动续费；0：未设置自动续费
        :type AutoRenewFlag: int
        :param DeadlineTime: 实例到期时间
        :type DeadlineTime: str
        """
        self.RedisName = None
        self.RedisId = None
        self.Appid = None
        self.ProjectId = None
        self.RegionId = None
        self.ZoneId = None
        self.VpcId = None
        self.UnVpcId = None
        self.SubnetId = None
        self.UnSubnetId = None
        self.Status = None
        self.StatusDesc = None
        self.WanIp = None
        self.Port = None
        self.Createtime = None
        self.Size = None
        self.SizeUsed = None
        self.TypeId = None
        self.TypeIddesc = None
        self.AutoRenewFlag = None
        self.DeadlineTime = None


    def _deserialize(self, params):
        self.RedisName = params.get("RedisName")
        self.RedisId = params.get("RedisId")
        self.Appid = params.get("Appid")
        self.ProjectId = params.get("ProjectId")
        self.RegionId = params.get("RegionId")
        self.ZoneId = params.get("ZoneId")
        self.VpcId = params.get("VpcId")
        self.UnVpcId = params.get("UnVpcId")
        self.SubnetId = params.get("SubnetId")
        self.UnSubnetId = params.get("UnSubnetId")
        self.Status = params.get("Status")
        self.StatusDesc = params.get("StatusDesc")
        self.WanIp = params.get("WanIp")
        self.Port = params.get("Port")
        self.Createtime = params.get("Createtime")
        self.Size = params.get("Size")
        self.SizeUsed = params.get("SizeUsed")
        self.TypeId = params.get("TypeId")
        self.TypeIddesc = params.get("TypeIddesc")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.DeadlineTime = params.get("DeadlineTime")


class RegionConf(AbstractModel):
    """地域配置

    """

    def __init__(self):
        """
        :param RegionId: 地域id 1--广州 4--上海 5-- 香港 6--多伦多 7--上海金融 8--北京 9-- 新加坡 11--深圳金融 15--美西（硅谷）
        :type RegionId: str
        :param Zones: 地域包含的区域
        :type Zones: :class:`tencentcloud.redis.v20180412.models.ZoneCapacity`
        """
        self.RegionId = None
        self.Zones = None


    def _deserialize(self, params):
        self.RegionId = params.get("RegionId")
        if params.get("Zones") is not None:
            self.Zones = ZoneCapacity()
            self.Zones._deserialize(params.get("Zones"))


class RenewRedisRequest(AbstractModel):
    """RenewRedis请求参数结构体

    """

    def __init__(self):
        """
        :param Period: 购买时长，单位：月
        :type Period: int
        :param RedisId: 实例串号
        :type RedisId: str
        """
        self.Period = None
        self.RedisId = None


    def _deserialize(self, params):
        self.Period = params.get("Period")
        self.RedisId = params.get("RedisId")


class RenewRedisResponse(AbstractModel):
    """RenewRedis返回参数结构体

    """

    def __init__(self):
        """
        :param DealId: 交易Id
        :type DealId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DealId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealId = params.get("DealId")
        self.RequestId = params.get("RequestId")


class ResetRedisPasswordRequest(AbstractModel):
    """ResetRedisPassword请求参数结构体

    """

    def __init__(self):
        """
        :param RedisId: 待操作的实例ID，可通过 DescribeRedis 接口返回值中的 redisId 获取。
        :type RedisId: str
        :param Password: 实例新密码，密码规则： 长度为8-16个字符；至少包含字母、数字和字符（!@#%^()）中的两种
        :type Password: str
        """
        self.RedisId = None
        self.Password = None


    def _deserialize(self, params):
        self.RedisId = params.get("RedisId")
        self.Password = params.get("Password")


class ResetRedisPasswordResponse(AbstractModel):
    """ResetRedisPassword返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RestoreInstanceRequest(AbstractModel):
    """RestoreInstance请求参数结构体

    """

    def __init__(self):
        """
        :param RedisId: 待操作的实例ID，可通过 DescribeRedis 接口返回值中的 redisId 获取。
        :type RedisId: str
        :param Password: 实例密码，恢复实例时，需要校验实例密码
        :type Password: str
        :param BackupId: 备份ID，可通过 GetRedisBackupList 接口返回值中的 backupId 获取
        :type BackupId: str
        """
        self.RedisId = None
        self.Password = None
        self.BackupId = None


    def _deserialize(self, params):
        self.RedisId = params.get("RedisId")
        self.Password = params.get("Password")
        self.BackupId = params.get("BackupId")


class RestoreInstanceResponse(AbstractModel):
    """RestoreInstance返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID，可通过 DescribeTaskInfo 接口查询任务执行状态
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class SetRedisAutoRenewRequest(AbstractModel):
    """SetRedisAutoRenew请求参数结构体

    """

    def __init__(self):
        """
        :param RedisIds: 实例 ID 组成的数组，数组下标从0开始
        :type RedisIds: list of str
        :param IsAutoRenew: 设置自动续费标识，0 - 不设置自动续费，实例到期会通知；1 - 设置自动续费，到期会自动续费；2 - 到期不续费也不通知
        :type IsAutoRenew: int
        """
        self.RedisIds = None
        self.IsAutoRenew = None


    def _deserialize(self, params):
        self.RedisIds = params.get("RedisIds")
        self.IsAutoRenew = params.get("IsAutoRenew")


class SetRedisAutoRenewResponse(AbstractModel):
    """SetRedisAutoRenew返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SlowlogDetail(AbstractModel):
    """慢日志信息

    """

    def __init__(self):
        """
        :param ExecTime: 执行时间
        :type ExecTime: str
        :param Duration: 执行持续时间
        :type Duration: int
        :param Command: 执行命令
        :type Command: str
        :param CmdLine: 执行整个命令
        :type CmdLine: str
        """
        self.ExecTime = None
        self.Duration = None
        self.Command = None
        self.CmdLine = None


    def _deserialize(self, params):
        self.ExecTime = params.get("ExecTime")
        self.Duration = params.get("Duration")
        self.Command = params.get("Command")
        self.CmdLine = params.get("CmdLine")


class TaskInfo(AbstractModel):
    """任务信息

    """

    def __init__(self):
        """
        :param StartTime: 任务的提交时间，格式如： 2017-02-10 16:56:18
        :type StartTime: str
        :param TaskType: 任务类型定义为 : '001'：task_newInstance：新建实例                                                                                                                                                                                                            '002'：task_resizeInstance：升级实例的任务 '004'：task_cleanInstance：清空实例的任务； '006'：task_deleteInstance：删除实例 '007'：task_setPassword'：设置密码 '008'：task_importRdb：导入Rdb的任务； '009'：task_exportBackup：导出备份的任务； '010'：task_restoreBackup：恢复实例的任务； '011'：task_restoreStream：回档实例的任务（集群版实例可回档3天内任意时间点，但是，最近10分钟的数据不可回档）； '012'：task_backupInstance：备份实例的任务；
        :type TaskType: str
        :param RedisName: 实例名称
        :type RedisName: str
        :param RedisId: 实例ID
        :type RedisId: str
        :param ProjectId: 实例所属的项目ID
        :type ProjectId: int
        :param Status: 任务执行状态，0：待执行；1：执行中；2：成功；3：失败；-1 执行出错
        :type Status: int
        :param Progress: 任务执行进度，0：未完成；1：已完成
        :type Progress: float
        :param TaskID: 任务流ID，用于查询任务详情。
        :type TaskID: int
        """
        self.StartTime = None
        self.TaskType = None
        self.RedisName = None
        self.RedisId = None
        self.ProjectId = None
        self.Status = None
        self.Progress = None
        self.TaskID = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.TaskType = params.get("TaskType")
        self.RedisName = params.get("RedisName")
        self.RedisId = params.get("RedisId")
        self.ProjectId = params.get("ProjectId")
        self.Status = params.get("Status")
        self.Progress = params.get("Progress")
        self.TaskID = params.get("TaskID")


class TestRequest(AbstractModel):
    """Test请求参数结构体

    """

    def __init__(self):
        """
        :param UserType: 无
        :type UserType: int
        """
        self.UserType = None


    def _deserialize(self, params):
        self.UserType = params.get("UserType")


class TestResponse(AbstractModel):
    """Test返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class TradeDealDetails(AbstractModel):
    """订单交易信息

    """

    def __init__(self):
        """
        :param DealId: 订单号ID，调用云API时使用此ID
        :type DealId: str
        :param DealName: 长订单ID，反馈订单问题给官方客服使用此ID
        :type DealName: str
        :param ZoneId: 可用区id
        :type ZoneId: int
        :param GoodsNum: 订单关联的实例数
        :type GoodsNum: int
        :param Creater: 创建用户uin
        :type Creater: str
        :param CreatTime: 订单创建时间
        :type CreatTime: str
        :param OverdueTime: 订单超时时间
        :type OverdueTime: str
        :param EndTime: 订单完成时间
        :type EndTime: str
        :param Status: 订单状态 1：未支付 2:已支付，未发货 3:发货中 4:发货成功 5:发货失败 6:已退款 7:已关闭订单 8:订单过期 9:订单已失效 10:产品已失效 11:代付拒绝 12:支付中
        :type Status: int
        :param Description: 订单状态描述
        :type Description: str
        :param Price: 订单实际总价，单位：分
        :type Price: int
        :param GoodsDetail: 返回的数组，不同订单的goodsDetail不相同
        :type GoodsDetail: list of GoodsDetail
        """
        self.DealId = None
        self.DealName = None
        self.ZoneId = None
        self.GoodsNum = None
        self.Creater = None
        self.CreatTime = None
        self.OverdueTime = None
        self.EndTime = None
        self.Status = None
        self.Description = None
        self.Price = None
        self.GoodsDetail = None


    def _deserialize(self, params):
        self.DealId = params.get("DealId")
        self.DealName = params.get("DealName")
        self.ZoneId = params.get("ZoneId")
        self.GoodsNum = params.get("GoodsNum")
        self.Creater = params.get("Creater")
        self.CreatTime = params.get("CreatTime")
        self.OverdueTime = params.get("OverdueTime")
        self.EndTime = params.get("EndTime")
        self.Status = params.get("Status")
        self.Description = params.get("Description")
        self.Price = params.get("Price")
        if params.get("GoodsDetail") is not None:
            self.GoodsDetail = []
            for item in params.get("GoodsDetail"):
                obj = GoodsDetail()
                obj._deserialize(item)
                self.GoodsDetail.append(obj)


class UpgradeRedisInquiryPriceRequest(AbstractModel):
    """UpgradeRedisInquiryPrice请求参数结构体

    """

    def __init__(self):
        """
        :param RedisId: 实例串号
        :type RedisId: str
        :param MemSize: 升级后的容量，1024的整数倍，单位：MB。升级后容量必须大于当前实例容量，大小限制以查询可售卖规格 为准
        :type MemSize: int
        :param BillingMode: 计费模式：0-按量计费，1-包年包月
        :type BillingMode: int
        """
        self.RedisId = None
        self.MemSize = None
        self.BillingMode = None


    def _deserialize(self, params):
        self.RedisId = params.get("RedisId")
        self.MemSize = params.get("MemSize")
        self.BillingMode = params.get("BillingMode")


class UpgradeRedisInquiryPriceResponse(AbstractModel):
    """UpgradeRedisInquiryPrice返回参数结构体

    """

    def __init__(self):
        """
        :param Price: 升级总费用，单位：分
        :type Price: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Price = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Price = params.get("Price")
        self.RequestId = params.get("RequestId")


class UpgradeRedisRequest(AbstractModel):
    """UpgradeRedis请求参数结构体

    """

    def __init__(self):
        """
        :param RedisId: 升级的实例Id
        :type RedisId: str
        :param MemSize: 规格 单位 MB, 计费侧GB
        :type MemSize: int
        """
        self.RedisId = None
        self.MemSize = None


    def _deserialize(self, params):
        self.RedisId = params.get("RedisId")
        self.MemSize = params.get("MemSize")


class UpgradeRedisResponse(AbstractModel):
    """UpgradeRedis返回参数结构体

    """

    def __init__(self):
        """
        :param DealId: 订单ID
        :type DealId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DealId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DealId = params.get("DealId")
        self.RequestId = params.get("RequestId")


class ZoneCapacity(AbstractModel):
    """区域不同类型的Redis的容量
    	Type		int64	`json:"Type"`			// 配置类型， 1 集群版， 2 单机版
    	TypeName	string	`json:"TypeName"` 		// 类型名称： 集群版， 单机版
    	MinMemSize 	int64 	`json:"MinMemSize"`		// 单位MB
    	MaxMemSize 	int64 	`json:"MaxMemSize"`		// 单位MB
    	MinBuyNum  	int64 	`json:"MinBuyNum"`
    	MaxBuyNum  	int64 	`json:"MaxBuyNum"`
    	Saleout		bool	`json:"Saleout"`        //是否售罄

    """

    def __init__(self):
        """
        :param TypeName: 实例类型名称
        :type TypeName: str
        :param MinMemSize: 单个实例最小容量，单位:MB
        :type MinMemSize: int
        :param Type: 实例类型，1 – 集群版；2 – 主从版；3-新一代主从版
        :type Type: int
        :param Saleout: 是否售罄
        :type Saleout: bool
        :param MaxBuyNum: 单次购买的最小实例数
        :type MaxBuyNum: int
        :param MinBuyNum: 单次购买的最大实例数
        :type MinBuyNum: int
        :param MaxMemSize: 单个实例最大容量，单位:MB
        :type MaxMemSize: int
        """
        self.TypeName = None
        self.MinMemSize = None
        self.Type = None
        self.Saleout = None
        self.MaxBuyNum = None
        self.MinBuyNum = None
        self.MaxMemSize = None


    def _deserialize(self, params):
        self.TypeName = params.get("TypeName")
        self.MinMemSize = params.get("MinMemSize")
        self.Type = params.get("Type")
        self.Saleout = params.get("Saleout")
        self.MaxBuyNum = params.get("MaxBuyNum")
        self.MinBuyNum = params.get("MinBuyNum")
        self.MaxMemSize = params.get("MaxMemSize")
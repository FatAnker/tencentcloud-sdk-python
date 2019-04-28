# Copyright 1999-2017 Tencent Ltd.
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

from tce.tcloud.utils.config import global_config
from QcloudApi.modules import base
region = global_config.get('regions')
params = global_config.get(region)
domain = params['domain_api2']

class CMQ(base.Base):
    requestHost = 'cmq.'+domain
    # requestHost = 'clb.api2.test.403a.tcecqpoc.fsphere.cn'

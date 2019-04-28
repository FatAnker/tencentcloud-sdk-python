#!/usr/bin/env python
# encoding: utf-8
global_config = {
    "regions": 'wh',
    "shanghai": {
        'secretId': 'AKIDylMjqkOq7Azay9Nq8D5kCSVM1Sfft4Sd',
        'secretKey': 'K8lBONAk7IEzXt30kGXcS5UfbJm0zkG4',
        'domain_api3': 'api3.test.403a.tcecqpoc.fsphere.cn',
        'domain_api2': 'api2.test.403a.tcecqpoc.fsphere.cn',
        'ZoneId': 50050001,
        "Uin": 100004603022,
        "AppId":1255000018
    },
    "chongqing": {
        'secretId': 'AKIDNIvEvaSP1Zmul0sd0SFYmggkZbvx7hGA',
        'secretKey': 'nMsFJ8FxlGWnloq8YfWjHomrCdST2LMm',
        'domain_api3': 'api3.401.tcecqpoc.fsphere.cn',
        'domain_api2': 'api2.401.tcecqpoc.fsphere.cn',
        'Zone_chongqing': 'chongqing401',
        'ZoneId':50040001,
        "Uin": 100004603027,
        "AppId": 1255000025
    },
    "wh": {
        'secretId': 'AKID5rUnkLJU2F6yVgoy5qFITImug6AsNeiQ',
        'secretKey': 'TaLknU9SP0F9ivmgFSJoxkBGRGjqb03k',
        'domain_api3': 'api3.401.tcecqpoc.fsphere.cn',
        'domain_api2': 'api2.401.tcecqpoc.fsphere.cn',
        'Zone_chongqing': 'chongqing401',
        'ZoneId': 50040001,
        "Uin": 100004603027,
        "AppId": 1255000025
    },
    "API_name": {
        "cbs": [
            "CreateDisks", "DescribeDisks", "AttachDisks", "DescribeDiskConfigQuota", "DescribeInstancesDiskNum",
            "ModifyDiskAttributes", "ResizeDisk", "CreateSnapshot",
            "CreateAutoSnapshotPolicy", "DescribeAutoSnapshotPolicies",
            "BindAutoSnapshotPolicy", "DescribeDiskAssociatedAutoSnapshotPolicy", "DescribeSnapshots"

        ],
    },

}
"""
, "ModifySnapshotAttribute",
            "ApplySnapshot", "UnbindAutoSnapshotPolicy", "DeleteAutoSnapshotPolicies", "DeleteSnapshots",
            "DetachDisks",
            "TerminateDisks"
"""

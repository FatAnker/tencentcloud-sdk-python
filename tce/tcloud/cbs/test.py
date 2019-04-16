from tce.tcloud.utils.config import global_config
region = global_config.get('regions')
params = global_config.get(region)

secretId = params['secretId']
secretKey = params['secretKey']
domain = params['domain']

url = "cbs." + domain
print(region)
print(url)
print(secretId)
print(secretKey)
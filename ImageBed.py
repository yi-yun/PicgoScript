# appid 已在配置中移除,请在参数 Bucket 中带上 appid。Bucket 由 bucketname-appid 组成
# 1. 设置用户配置, 包括 secretId，secretKey 以及 Region
# -*- coding=utf-8
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
import sys
import logging
import time
import appex
import clipboard

def get_image():
	if not appex.is_running_extension():
		print('This script is intended to be run from the sharing extension.')
		return
	images = appex.get_attachments('public.jpeg')
	return images[0]


logging.basicConfig(level=logging.INFO, stream=sys.stdout)

secret_id = ''      # 替换为用户的 secretId
secret_key = ''      # 替换为用户的 secretKey
region = ''     # 替换为用户的 Region
token = None                # 使用临时密钥需要传入 Token，默认为空，可不填
scheme = 'https'            # 指定使用 http/https 协议来访问 COS，默认为 https，可不填
config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key, Token=token, Scheme=scheme)
# 2. 获取客户端对象
client = CosS3Client(config)
time_name = time.strftime("%Y%m%d%H%M%S",time.localtime(time.time()))
response = client.put_object_from_local_file(
    Bucket='',
    LocalFilePath=get_image(),
    Key=time_name+'.jpg'
)
print(response['ETag'])
link = '![]('+time_name+'.jpg'+')'
clipboard.set(link)
print('复制到剪贴板成功！')

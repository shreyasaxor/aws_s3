import boto3
from botocore.client import Config

ACCESS_KEY_ID = 'AKIAIY6TEJKN4SYG75YQ'
ACCESS_SECRET_KEY = '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'
BUCKET_NAME = 'shreyasnivya'




bucket=BUCKET_NAME
key='bitmoji.png'

try:
	s3 = boto3.resource('s3',
		    aws_access_key_id=ACCESS_KEY_ID,
		    aws_secret_access_key=ACCESS_SECRET_KEY,
		    config=Config(signature_version='s3v4'))
	obj = s3.Object(bucket, key)
	a = obj.get()['Body'].read()
	print(a)
except:
	import sys
	print(sys.exe_info())

print ("Done")
	

import boto3
from botocore.client import Config

ACCESS_KEY_ID = 'AKIAIY6TEJKN4SYG75YQ'
ACCESS_SECRET_KEY = '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'
BUCKET_NAME = 'shreyasnivya'


try:
	data = open('hiiiii.jpg', 'rb')
	s3 = boto3.resource(
	    's3',
	    aws_access_key_id=ACCESS_KEY_ID,
	    aws_secret_access_key=ACCESS_SECRET_KEY,
	    config=Config(signature_version='s3v4')
	)
	s3.Bucket(BUCKET_NAME).put_object(Key='bitmoji.png', Body=data)
except:
	import sys
	print(sys.exe_info())

print ("Done")





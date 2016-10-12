from S3Client import S3Client

# create configuration
config = dict()
config['service'] = 's3'
config['url'] = 's3.example.cluster'
config['access_key'] = 'aaaaaaaaaaaaaaa'
config['secret_key'] = 'bbbbbbbbbbbbbbb'
config['s3_bucket'] = 'example'
config['s3_key'] = '/path_example/example/'

# load configuration
S3Client.load_config(config)

# upload files to s3
file_1 = 'myfiletest.exe'
file_2 = 'example.exe'

S3Client.upload_s3(file_1)
S3Client.upload_s3(file_2)

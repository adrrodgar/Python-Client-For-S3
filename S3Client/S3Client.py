import boto3
from botocore.utils import fix_s3_host

class S3Client():

    configuration = None

    # Method to load configuration for S3
    @staticmethod
    def load_config(config):
        S3Client.configuration = config
    

    # Method to upload files to S3
    @staticmethod
    def upload_s3(filename):

        try:
            # connect to hosts.
            s3resource = boto3.resource(service_name=S3Client.configuration['service'],
                                verify=False,
                                endpoint_url=S3Client.configuration['url'],
                                aws_access_key_id=S3Client.configuration['access_key'],
                                aws_secret_access_key=S3Client.configuration['secret_key'])

            # Avoid redirect
            s3resource.meta.client.meta.events.unregister('before-sign.s3', fix_s3_host)

            # Get bucket
            bucket = s3resource.Bucket(S3Client.configuration['s3_bucket'])
            data = open(filename, 'rb')

            # upload file to riak
            bucket.put_object(Key=S3Client.configuration['s3_key'] + filename, Body=data)

            # close file
            data.close()
            print("File: ", filename, " has been upload successfully")
        
        except Exception as e:
            print(e)

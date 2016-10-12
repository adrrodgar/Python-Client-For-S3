# Python Client for S3

This project help you to upload files to your own cluster of S3.

## Install

The recommended versions of Python for use with this client are Python 3.4.x and 3.5.x.

### From PyPI

Official packages are signed and published to PyPI.
To install from PyPI directly you can use pip.

```
pip install boto3
```

## Testing

In first place, it's necessary configure the client in test script to connect the client with the cluster.
* [service] - The service used.
* [url] - Cluster direction.
* [access key and secret key] - User's credentials.
* [s3 bucket] -  Logical unit of storage in S3 object storage service.
* [S3 key] - Bucket path where storage data

```
config = dict()
config['service'] = 's3'
config['url'] = 's3.example.cluster'
config['access_key'] = 'aaaaaaaaaaaaaaa'
config['secret_key'] = 'bbbbbbbbbbbbbbb'
config['s3_bucket'] = 'example'
config['s3_key'] = '/path_example/example/'
```

Then select the files you want to upload to S3.

```
file_1 = 'myfiletest.exe'
file_2 = 'example.exe'
```

Finally, execute the script.

```
python test.py
```



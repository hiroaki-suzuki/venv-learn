import boto3
import pprint

if __name__ == '__main__':
    client = boto3.client('s3')
    response = client.list_buckets()
    pprint.pprint(response['Buckets'])

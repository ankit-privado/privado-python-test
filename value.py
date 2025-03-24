import boto3

OPTIMIZELY_EVENTS_BUCKET = "mera-bucket"

def get_s3():
    return boto3.resource(
        's3',
        aws_access_key_id="ID",
        aws_secret_access_key="KEY",
    )

bucket = get_s3().Bucket(OPTIMIZELY_EVENTS_BUCKET)

import json
import boto3 

def lambda_handler(event, context):
    client = boto3.client("glue")

    client.start_job_run(
        JobName = 'honGlueJob',
        Arguments = {}
    )
    return {
        'statusCode': 200,
        'body': json.dumps('honGlueJob triggered')
    }
    
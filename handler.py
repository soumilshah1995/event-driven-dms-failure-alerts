# Import modules
import boto3
import json
import os
import logging

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)
# Set up Boto 3 client for SNS
client = boto3.client(
    'sns',
    aws_access_key_id=os.getenv("DEV_ACCESS_KEY"),
    aws_secret_access_key=os.getenv("DEV_SECRET_KEY"),
    region_name=os.getenv("DEV_REGION"),
)
# Variables for the SNS:
snsTopicARN = os.getenv("TopicArn")


# Define Lambda function
def lambda_handler(event, context):
    logger.info('## INITIATED BY EVENT: ')
    logger.info(event['detail'])
    print(event)

    response = client.publish(
        TargetArn=snsTopicARN,
        Message=json.dumps({'default': json.dumps(event)}),
        Subject='An DMS Task  has failed',
        MessageStructure='json')

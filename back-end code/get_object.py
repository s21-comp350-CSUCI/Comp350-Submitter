import json
import boto3

sqs_client = boto3.client('sqs')
QueueUrl = "https://sqs.us-east-1.amazonaws.com/208939558331/submitter_sqs"
sqs_response = sqs_client.receive_message(
    QueueUrl=QueueUrl,
    AttributeNames=[
        'SentTimestamp'
    ],
    MaxNumberOfMessages=1,
    MessageAttributeNames=[
        'All'
    ],
    VisibilityTimeout=15,
    WaitTimeSeconds=0
)

message = sqs_response['Messages'][0] #get message from sqs queue
filename = message['filename'] #get filename from message
bucket_name = 'comp350-submitter-bucket' #bucket name

s3_client = boto3.client('s3')
s3_response = s3_client.get_object(Bucket=bucket_name, Key=filename) #get object from bucket

#use s3_response to process object?





#delete message
receipt_handle = message['ReceiptHandle']
sqs_client.delete_message(
    QueueUrl=QueueUrl,
    ReceiptHandle=receipt_handle
)

#sqs queue name: submitter_sqs
#sqs queue url: https://sqs.us-east-1.amazonaws.com/208939558331/submitter_sqs

#s3 bucket name: comp350-submitter-bucket
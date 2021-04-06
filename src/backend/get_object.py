import json # data representation format
import boto3 # AWS SDK for Python

sqs_client = boto3.client('sqs') # create sqs client to use its receive message method
QueueUrl = "https://sqs.us-east-1.amazonaws.com/208939558331/submitter_sqs" # queue url

# Retrieves one message from the specified queue.
sqs_response = sqs_client.receive_message(
    # The URL of the Amazon SQS queue from which messages are received
    QueueUrl=QueueUrl,

    # A list of attributes that need to be returned along with each message
    AttributeNames=[
        'SentTimestamp' # Returns the time the message was sent to the queue (epoch time in milliseconds)
    ],

    MaxNumberOfMessages=1, # The maximum number of messages to return

    # The name of the message attribute
    MessageAttributeNames=[
        'All' # return all of the attributes
    ],
    VisibilityTimeout=15, # The duration (in seconds) that the received messages are hidden from subsequent retrieve
                          # requests after being retrieved by a ReceiveMessage request
    WaitTimeSeconds=0 # The duration (in seconds) for which the call waits for a message to arrive in the queue before returning
)

message = sqs_response['Messages'][0] #get message from sqs queue
filename = message['filename'] #get filename from message - (need to change based on json format)

bucket_name = 'comp350-submitter-bucket' #bucket name

s3_client = boto3.client('s3') # create s3 client to use its get object method
s3_response = s3_client.get_object(Bucket=bucket_name, Key=filename) #get object from bucket

#use s3_response to process object
    #<insert code here>

#delete message from sqs queue
receipt_handle = message['ReceiptHandle']
sqs_client.delete_message(
    QueueUrl=QueueUrl,
    ReceiptHandle=receipt_handle
)

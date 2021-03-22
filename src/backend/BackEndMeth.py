import json
import boto3


#sqs_client = boto3.client('sqs')
#QueueUrl = "https://sqs.us-east-1.amazonaws.com/208939558331/submitter_sqs"
#bucket_name = 'comp350-submitter-bucket'
#s3_client = boto3.client('s3')



def retrieveMessageFromQueue(sqsClient, queURL):
    
    sqs_response = sqs_client.receive_message(
        QueueUrl=QueueUrl,
        AttributeNames=[
            'SentTimestamp'
        ],
        MaxNumberOfMessages=1,
        MessageAttributeNames=[
            'All'
        ],
        VisibilityTimeout=150,
        WaitTimeSeconds=0
    )

    message = sqs_response['Messages'][0] #get message from sqs queue
    return message


def retrieveObjectFromBucket(s3bucket='comp350-submitter-bucket' , filename):
    s3_response = s3_client.get_object(Bucket=s3bucket, Key=filename)
    return s3_response




def deleteMessageFromQueue(sqsClient, queURL, message):
    #delete message
    receipt_handle = message['ReceiptHandle']
    sqs_client.delete_message(
        QueueUrl=QueueUrl,
        ReceiptHandle=receipt_handle
    )



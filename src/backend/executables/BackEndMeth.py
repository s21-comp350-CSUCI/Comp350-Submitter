import json
import boto3
import hashlib
import sys

#sqs_client = boto3.client('sqs')
#QueueUrl = "https://sqs.us-east-1.amazonaws.com/208939558331/submitter_sqs"
#bucket_name = 'comp350-submitter-bucket'
#s3_client = boto3.client('s3')

# Takes an sqs client and the url for the sqs queue. 
# Returns ENTIRE message from the named queue. 
# Uses a visibility timeout of 150
def retrieveMessageFromQueue(sqsClient, queURL):
    sqs_response = sqsClient.receive_message(
        QueueUrl=queURL,
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
    return message


# Takes the client and url of the message to delete, and the message.
# Uses the message handle from the message object to delete.
def deleteMessageFromQueue(sqsClient, queURL, message):
    receipt_handle = message['ReceiptHandle']
    sqsClient.delete_message(
        QueueUrl=queURL,
        ReceiptHandle=receipt_handle
    )



# This function takes the name of the object to download, the name of the file to save it as,
# the s3 client, and the bucket name. It returns a response.
def retrieveObjectFromBucket(objname, dstname, s3client, s3bucket='comp350-submitter-bucket'):
    s3_response = s3client.download_file(s3bucket, srcname, dstname)
    return s3_response

# This function will create a unique 128-bit token 
# for a student to use for submitting code to an event.
def createStudentToken(studentEmail, adminName, eventName):
    stringToken = "{}:{}:{}".format(studentEmail, adminName, eventName)
    token = hashlib.md5(stringToken.encode()).hexdigest()
    return token

# This function will generate a unique submission id
# for the student tokens provided unque to the students,
# the admin, event, and specific problem
def createSubmissionID(tokenList, adminName, eventName, problemName):
    tokenList.sort()
    stringToken = "{}:{}:{}:{}".format(*tokenList, adminName, eventName, problemName)
    token = hashlib.md5(stringToken.encode()).hexdigest()
    return token

# To create a unique name for a test.in or test.out file, it should be unique to 
# the assignemnt it corresponds to, which in turn is unique to an event, and events are uniqu to admins.
# i.e. def createTestCaseFileName("in", "m.soltys", "350", "Assignemnt 16") gives you 
# a unique hash for an input file. 
def createTestCaseFileName(inorout, adminName, eventName, problemName):
    stringToken = "{}:{}:{}:{}".format("test.in" if inorout == "in" else "test.out", \
      adminName, eventName, problemName)
    token = hashlib.md5(stringToken.encode()).hexdigest()
    return token

# This function takes a json file and returns a python dictionary
# then it will call the appropriate function to process the submission/event
def getJsonDict(json_file):
    # converts json to python dictionary
    return json.loads(json_file)


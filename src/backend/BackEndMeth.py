import json
import boto3
import hashlib
import sys
import os


# sqs_client = boto3.client('sqs')
# QueueUrl = "https://sqs.us-east-1.amazonaws.com/208939558331/submitter_sqs"
# bucket_name = 'comp350-submitter-bucket'
# s3_client = boto3.client('s3')


# This function will return a message in
# json format from the sqs queue
def retrieveMessageFromQueue(sqsClient, queURL):
    # Visibility timeout starting at 150, since it is better to have
    # to shorten it, then we have an error because too short. Once we 
    # know the longest time it takes to process a job, we set the 
    # timeout to just over that.
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

    message = sqs_response['Messages'][0]  # get message from sqs queue
    return message


# This function deletes a message from the queue (to be done
# upon completion of task, else message is visible on queue again)
def deleteMessageFromQueue(sqsClient, queURL, message):
    # delete message
    receipt_handle = message['ReceiptHandle']
    sqsClient.delete_message(
        QueueUrl=queURL,
        ReceiptHandle=receipt_handle
    )


# This function will return an object (json, py, etc)
# from a named bucket or default 
def retrieveObjectFromBucket(obj, s3client, s3bucket='comp350-submitter-bucket'):
    s3_response = s3client.get_object(Bucket=s3bucket, Key=obj)
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


# This function takes a json file and returns a python dictionary
# then it will call the appropriate function to process the submission/event
def getJsonDict(json_file):
    # converts json to python dictionary
    return json.loads(json_file)


# This function will poll from the SQS until a message is received
# and returns the message otherwise continues
def pollSQS(sqsClient, queueURL):
    while True:
        message = retrieveMessageFromQueue(sqsClient, queueURL)
        if message:
            return message
        else:
            continue


# This function takes the absolute path and then returns the parent directory
# by calling the appropriate function
def extractParentDirectory(subdata_path):
    return os.path.dirname(subdata_path)


# This functions concatenates the absolute path with the file name and returns it
def buildPathName(path_dir, file_name):
    return path_dir + "/" + file_name


# This functions extracts the assignment information from the python dictionary
# and returns the information in a python tuple
def extractAssignmentInfo(json_dict):
    admin = json_dict.get("admin")
    event = json_dict.get("event")
    assignment = json_dict.get("problem")
    submissionID = json_dict.get("submissionid")

    testInPath = "/home/ec2-user/" + submissionID + "/test.in"
    testOutPath = "/home/ec2-user/" + submissionID + "/test.out"

    assignmentInfoTuple = (admin, event, assignment, testInPath, testOutPath)

    return assignmentInfoTuple

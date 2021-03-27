import json
import os
import BackEndMeth


# the object is a json file with all the info for a student and admin
# i.e. submission and event json w/ all event parameters

# This function will process the json file and load it into a python dictionary
# then it will call the appropriate function to process the submission/event
def processJsonFile(json_file):
    # converts json to python dictionary
    message_dict = json.loads(json_file)

    # if the "tokens" key exists in the dictionary then process student otherwise process admin
    if "tokens" in message_dict:
        processStudent(message_dict)
    else:
        processAdmin(message_dict)


# This function processes the event that was loaded into a python dictionary
# then it saves the event in the RDS & creates/sends tokens to all students via SNS
def processAdmin(message_dict):
    # process the event (based off eventExample.json)
    event = message_dict.get("event")
    adminName = event.get("admin")
    eventName = event.get("name")
    parameters = event.get("parameters")
    emails = message_dict.get("emails")

    # save event to RDS
    # function goes here

    # create tokens for every student
    for studentEmail in emails:
        token = createStudentToken(studentEmail, adminName, eventName)
        # send token to student via SNS
    # function goes here


# This function processes the submission that was loaded into a python dictionary
# then it runs the test cases in a docker. If it is successful then it creates a
# submission ID so it can be added to the grade test queue
def processStudent(message_dict):
    # process the submission (based off subExample.json)
    submission = message_dict.get("submission")
    eventName = submission.get("event")
    adminName = submission.get("admin")
    tokenList = message_dict.get("tokens")
    subID = message_dict.get("subID")
    code = message_dict.get("code")

    # run test cases (in docker container)
    docker_cmd = "docker run -it --rm --name='my-hello-world' -v '$PWD':/usr/src/myapp -w /usr/src/myapp python:3 python --version"
    docker = os.system(docker_cmd)

    # if docker was successful then create submission ID & place the submission in another queue
    # this way students will be able to submit multiple times before the deadline
    if docker is 0:
        print("successful")
        token_submission_id = createSubmissionID(tokenList, adminName, eventName, problemName)
        addToGradeCaseQueue(token_submission_id)
    else:
        # this may happen if file has major errors or file does not exists
        # Example: syntax
        print("unsuccessful")


# This function will add the submission to the grade cse queue. If the student has
# submitted before then it overwrites the old submission with the new submission
def addToGradeCaseQueue(submission):
    print(submission)


# This function will run each submissions in the grade case queue and save the results
# to the RDS for each student.
def processGradeCaseQueue():
    print("process grade case queue")

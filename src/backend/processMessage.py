import json
import os
import threading
import Queue


# The s3_response is a json file with all the info for a student submission
# i.e submission_example.json

# This functions runs the docker and places the results in a queue
def workerThread(docker_cmd, queue):
    docker = os.system(docker_cmd)
    queue.put(docker)


# What is this main thread used for?
def mainThread():
    print("main thread")


# This function processes the student submission. The message is extracted from the SQS and placed in subdata.
# We use subdata to open the json file and load it into a python dictionary named subdata_dictionary. From there
# the subid is extracted from the json file which will be used to make the directory and retrieve the objects
# from the S3 bucket. The test case parameters are then quarried and generate files for comparison. The docker
# is then ran and returns the results via a queue.
def runStudentSubmission(s3_response):
    # extracts the name of the json file from the SQS message
    # /submissions/m.soltys/aws_labs/lab5_containers/fc55c0190dde2bc413d8d1e79fb8cca2/fc55c0190dde2bc413d8d1e79fb8cca2.json
    subdata = s3_response.get("subdata")

    # open subdata (json file) and load it into a dictionary
    with open(subdata) as json_file:
        subdata_dictionary = json.load(json_file)

    # subid is assigned the submissionid and directory name is assigned by using the subid
    subid = subdata_dictionary.get("submissionid")
    directory_name = "/home/ec2-user/" + subid + "/"

    # creates directories from the directory name
    os.mkdirs(directory_name)

    # changing present working directories into the newly created directory
    os.chdir(directory_name)

    # Retrieve both the newly submitted json and python files from the S3 bucket
    json_object_name = directory_name + subid + ".json"
    python_object_name = directory_name + subid + ".py"
    json_file = retrieveObjectFromBucket(json_object_name, s3client, s3bucket='comp350-submitter-bucket')
    python_file = retrieveObjectFromBucket(python_object_name, s3client, s3bucket='comp350-submitter-bucket')

    # Query database for test case parameters
    # code goes here (RDS function?)

    # execute submitted code in Python 3.9 container
    # create MAIN thread and wait for the worker thread to finish executing before moving on
    docker_cmd = "docker run -it --rm --name='subid" + subid + "' -v '$PWD':/usr/src/submitter -w /usr/src/submitter python:3.9 executeSubmission.py " + subid

    # created a queue to return output from worker thread
    queue = Queue.Queue()
    worker_thread = Thread(target=workerThread, args=(docker_cmd, queue,))
    main_thread = Thread(target=mainThread)

    # runs the worker thread
    worker_thread = start()
    # waits for the worker thread to finish and joins
    worker_thread.join()
    # gets the results from queue that was placed by the worker thread
    worker_thread_result = queue.get()

    # runs the main thread : what is the main thread used for?
    main_thread = start()
    # waits for the main thread to finish and joins
    main_thread.join()

    # checks if the docker was ran successfully
    if worker_thread_result is 0:
        print("successful")
    else:
        # this may happen if file has major errors or file does not exists
        # Example: syntax
        print("unsuccessful")

#!/bin/python3
# https://realpython.com/intro-to-python-threading/#conclusion-threading-in-python
import threading
import os

class ClientThread(threading.Thread):
  def __init__(self,msg):
    threading.Thread.__init__(self)
    # The message from the SQS queue
    self.message = msg
    # Return a python dict
    msgDict = self.getJsonDict(self.message)
    # Path to subID.json in S3 bucket 
    self.subdata = self.extractDataFilePath(msgDict)
    # Submission ID unique to Admin/event/assignment/tokens.
    self.subID = os.path.basename(msgDict["Messages"][0]["Body"]["subdata"]).rstrip(".json")
    # Working directory name
    self.workingDirectory = "/usr/app/submission/{}/".format(self.subID)
    # Test input full path file name
    self.testIn = None
    # Test output full path file name 
    self.testOut = None
    # The student subID.py
    self.studentSubmission = None
    # Admin name
    self.adminName = None
    # Event name
    self.eventName = None
    # Assignemnt name
    self.assignmentName = None
    # Email addresses corresponding to submission tokens.
    self.studentEmailList = None



  def run(self):
    # If the dir exists, another thread is still running a previous submission
    while os.path.isdir(workingDirectory):
      assert not os.path.dir(self.workingDirectory), "Bug. Directory {} exists. Second submission \
       submitted before first graded?.".format(self.workingDirectory)
       continue
    # Create the working directory and change into it.
    os.mkdir(workingDirectory)
    os.chdir(workingDirectory)

    # retrieve the json file and place it in the current directory
    res_json = retrieveObjectFromBucket(self.subdata, "{}/{}.json".format(self.workingDirectory, self.subID), s3client, s3bucket='comp350-submitter-bucket')


#########################################################################
######################################################################### 
  

def main():
  
  
  
  while True:
    # Poll for a message on the queue
    message = pollSQS()
    t = ClientThread(message)
    t.start()
    continue

  
if __name__ == "__main__":
    main()

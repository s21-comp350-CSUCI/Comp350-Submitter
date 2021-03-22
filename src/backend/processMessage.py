import json
import boto3
import hashlib

# the object (message) is a json file with all the info for a student and admin
# i.e. submitted code and event object w/ all event parameters

def processJSONMessage(message):
	message_dict = json.loads(message)

	# prints dictionary
	# message_json = json.dumps(message_dict)
	# print(message_json)

	if "token" in message_dict:
		processStudent(message_dict)
	else:
		processAdmin(message_dict)


def processAdmin(message_dict):
    # process the events
	events = message_dict.get("events")
	for event in events:
		# save events to RDS - how are we storing/organizing



	# create tokens
	emails = message_dict.get("emails")
	for email in emails:
		token = hashlib.md5("stuff to be hashed here").hexdigest()
		# send tokens to students via SNS


def processStudent(message_dict):
	# process the files
	files = message_dict.get("files")

	# run test cases (in docker container) if it fails report to frontend and abort

	if docker is None:
		# this may happen if files have major errors
	else:
		for file in files:
			# run docker with test cases
			# return results to frontend

   
	# at this point docker did not fail and will place the files in another queue
	# this way students will be able to submit multiple times before the deadline
	addToGradeCaseQueue(files)


def addToGradeCaseQueue(files):
	# retrieve student credentials and store grade in RDS


def processGradeCaseQueue():
	files = message_dict.get("files")
	for file in files:
		# run docker with grade cases
		# once it is done with grade cases it return results to RDS 
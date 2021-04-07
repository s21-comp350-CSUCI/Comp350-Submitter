#!/usr/local/bin/python3
# This script will be run in a docker container executed with docker run,
# note the container specific path to python3 on first line.
import sys
import csv
import os
import subprocess
# helper function that opens a file and places each line 
# in a list, and returns the lest.
def returnFileAsList(file):
  # Open and read from test.in into inputList
  with open(file) as f:
    fileList = f.readlines()
  # Removing whitespace and clean up newlines
  fileList = [x.strip() for x in fileList]
  return fileList


# Check to make sure script is executed with correct number of arguments
if len(sys.argv) < 2 or len(sys.argv) > 2:
  print("Usage: ./executeSubmission.py <subID in form of MD5 hash>")
  sys.exit(1)

# This script will take a subID passed to it as a command line argument.
subID = str(sys.argv[1])

# Relevant file names
inFileName = "./test.in"
outFileName = "test.out"
subFileName = subID + ".py"
outputfilecsv = subID + ".out"

# Change current working directory to /usr/src/submitter (should be there already)
workingDirectory = "/usr/src/submitter"
os.chdir(workingDirectory)

# Open and read from test.in into inputList
inputList = returnFileAsList(inFileName)

# Open and read from test.out into outputList
outputList = returnFileAsList(outFileName)

# Open for writing to a file called subID.out, overwrite
with open(outputfilecsv, mode='w') as csvFile:
  # Define the field headers
  fields = ['input', 'expected output', 'actual output', 'pass/fail']
  writer = csv.DictWriter(csvFile, fieldnames=fields)
  # Write the first row header fields
  writer.writeheader()
  # In a loop execute subID.py with an input from the input array,
  # using subprocesses so that the return code, stdout and stderr can all 
  # captured. 
  for i in range(len(inputList)):
    # Define command as string
    cmd = "{} {} {}".format("python3", subFileName, inputList[i]) 
    
    # This will execute the command after calling a bash shell
    sp = subprocess.Popen(cmd,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)

    # Capture the return code (recall, subprocess is a new thread)
    rc = sp.wait()

    # Separate the output and error by communicating with sp variable.
    # This is similar to Tuple where we store two values to two different variables
    out,err=sp.communicate()
    # rstrip() is used to strip a single trailing whitespace that is added by the print() function.
    out, err = out.decode().rstrip(), err.decode().rstrip()
    # rc and stderr are here for future proofing,
    # in case in the future these can be communicated to the submitter.
    # Is the output what it should be
    result = "Pass" if str(out) == str(outputList[i]) else "Fail"
    
    # Write the row to csvFile
    writer.writerow({fields[0]: str(inputList[i]), fields[1]: str(outputList[i]), fields[2]: str(out), fields[3]: result})
  

# Successfully completed
exit()
    





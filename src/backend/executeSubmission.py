#!/usr/local/bin/python3
# This script will be run in a docker container executed with docker run,
# note the container specific path to python3 on first line.
import os
import sys
import csv

# Check to make sure script is executed with correct number of arguments
if len(sys.argv) < 2 or len(sys.argv) > 2:
  print("Usage: ./executeSubmission.py <subID in form of MD5 hash>")
  sys.exit(1)

# This script will take a subID passed to it as a command line argument.
subID = str(sys.argv[1])

# Relevant file names
inFileName = "test.in"
outfileName = "test.out"
subName = subID + ".py"

# Change current working directory to /usr/src/submitter (should be there already)
workingDirectory = "/usr/src/submitter"
os.chdir(workingDirectory)

# Open and read from test.in into inputList
with open(inFileName) as inf:
    inputList = inf.readlines()
# Removing whitespace and clean up newlines
inputList = [x.strip() for x in content] 

# Open and read from test.out into outputList
with open(outFileName) as outf:
    outputList = outf.readlines()
# Removing whitespace and clean up newlines
outputList = [x.strip() for x in content] 

# Open for writing to a file called subID.out

# In a loop execute subID.py with an input from the input array,
# using subprocesses so that the return code, stdout and stderr can all 
# captured. 

# For each input element create an entry in subID.out with input, expected output, output, pass/fail fields.

# Close all files and exit successfully.




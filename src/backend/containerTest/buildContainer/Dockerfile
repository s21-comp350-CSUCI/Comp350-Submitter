# Start with base image python 3.9
FROM python:3.9   
# Set the working directory of the image
WORKDIR /usr/src/submitter
# Copy the ./executeSubmission from host to cwd of the container ( We will see lol)
COPY ./executeSubmission.py /usr/local/bin/
# ./executeSubmission.py needs to be executable, but docker copies files into image with
# ther permissions they already have. Make sure ./executeSubmission.py is 755 before
# executing docker build


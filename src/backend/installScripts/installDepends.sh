#!/bin/bash
# This script will install Docker, Python 3, pip3, and boto3
# and must be setuid root owned program.
# When the ec2 instance spins up, the user data should include a mechanism to pull this directory and execute this script before anything else.

clear
echo "Installing Docker..."

sudo yum update -y
# installing
echo "Installing docker and dependencies..."
sudo amazon-linux-extras install docker -y
echo "Starting the Docker service"
sudo service docker start
echo "Adding $USER to Docker group"
sudo usermod -a -G docker ec2-user
echo "Enabling Docker service on boot..."
sudo systemctl enable docker
# pull the base image for our container
docker pull python:3.9
# installing python3, pip3, setuptools
sudo yum install python3-pip python3 python3-setuptools -y
# Install boto3
pip3 install boto3 --user
# Display version information
docker --version
python3 --version
pip3 --version

# Install git
sudo yum install git -y


# How our subexecutor image is created
## It is all layers
Containers are built in layers, from base image on top of base image. In our use case, we started with an official python 3.9 docker [image](https://hub.docker.com/_/python/).  

_It is important to note that before we begin to create our specific image, that docker is installed, and the python 3.9 docker image is pulled to the host._  

Now inside of a directory that contains only a Dockerfile and the python executable we want our container to have a copy of, open the dockerfile. We need 3 lines.

`FROM python:3.9 `  
This lays down a foundational layer- we are using the python:3.9 image as a starting template.  

`WORKDIR /usr/src/submitter`  
This sets the containers current directory. The copy command below use this working directory as its relative starting point.  

`COPY ./executeSubmission.py /usr/bin/`  
This will copy ./executeSubmission.py from the _docker context_ (the directory that the host called `docker build `  from) into the `/usr/local/bin` directory of the container. This choice was made because `./executeSubmission.py` needs to be executable, and `/usr/local/bin` is the first directory in the container's PATH variable.  
 

## Now build the image  
Now that the docker file is written, make sure the file to copy, `./executeSubmission.py` is in the same directory with +x or 755 priveleges. We call this container subexecutor, so we build it with   
`build -t subexecutor .`  
This tags the container as subexecutor with a default `latest` build. We can maintain differenct versions like this  
`build -t subexecutor:version_name . `  

## Pat attention  
_Sticky Points_  
* `COPY ` will copy a file from the source to the destination and retain the file permissions.
* A bind:mount will wipe out any existing directory of the name bind:mounted before binding and mounting, and if the directory does not exist in either the host or the container, it is created then bound and mounted. _THIS MEANS DO NOT USE COPY TO COPY A FILE INTO A DIRECTORY THAT WILL LATER BE BOUND AND MOUNTED, IT WILL BE ERASED._  


__subexecutor Dockerfile__  
```
FROM python:3.9   
WORKDIR /usr/src/submitter
COPY ./executeSubmission.py /usr/local/bin/
```

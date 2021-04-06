#!/bin/python3
# https://realpython.com/intro-to-python-threading/#conclusion-threading-in-python
# server.py - a simple threaded server
import threading



class ClientThread(threading.Thread):
  def __init__(self, subID):
    threading.Thread.__init__(self)
    self.subID = subID

  def run(self):
    # This is the entry point for the thread. At this point in the code
    # the constructor has executed
    pass

  pass
  # All the functionality described in backendmeth.md
  # Will be defined and executed in this thread class

#########################################################################
#########################################################################
  
def main():
  
  
  
  while True:
    # Poll for a message on the queue
    newMessage = pollSQS()
    # retrieve the subID from the json formated newMessage
    subID = extractSubID(newMessage)
    # pass the subID off to a worker thread and move on
    t = ClientThread(subID)
    t.start()
    continue

  
if __name__ == "__main__":
    main()

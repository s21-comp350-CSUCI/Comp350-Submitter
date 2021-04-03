import logging

import pymysql
from django import db

#  connection to data base
from RDS import cursor


def connect():
    db_connect = pymysql.connect(
        host = "new-submitter-rds.cmawzoprxmnb.us-east-1.rds.amazonaws.com",
        user = "admin",
        password = "comp350_rds",
        database = "new-submitter-rds"
    )
    return db_connect

#  event string format
def eventStringFrotmat(adminId, eventName, startDate, endDate):
    return "The admin is " + str(adminId) + ", event = " + str(eventName) + ", start date: " + str(startDate) + ", end date" + str(endDate) + "."

# insert Event
def insertEvent(eventEntry):
    # connects to db
    db_connect = connect()
    sqlCommiter = db_connect.cursor()

    # Not sure whats going to split the string change delimiter to appropriately format
    splitString = str(eventEntry).split('/t,', 4)
    adminId = splitString[0]
    eventName = splitString[1]
    startDate = splitString[2]
    endDate = splitString[3]

    sqlCommiter.execute("INSERT INTO event (adminId, eventName, startDate, endDate) VALUES (%s, %s, %s, %s) ",
                            (adminId, eventName, startDate, endDate))
    db_connect.commit()
    db_connect.close()
    sqlCommiter.close()


 def deleteEvent(eventEntry):
            db_connect = connect()
            cursor = db_connect.cursor()

            #deletes were based on just the unique id of the thing, the comment is the sql format for it
            #delete that entry
            cursor.execute("DELETE FROM event WHERE event_id = \""+ str(eventEntry) + "\"")
            db_connect.commit()
            cursor.close()
            db_connect.close()

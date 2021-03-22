
# Access AWS RDS with Python 3
# DB instance identifier: rds
# username: admin
# pass:
# host: rds.cmawzoprxmnb.us-east-1.rds.amazonaws.com
# port: 3306
# Availability zone: us-east-1a

# import boto3
# import json
import pymysql
from django import db

pymysql.connect('<host FMI>', '<username FMI>', '<pass FMI>')
cursor = db.cursor()
cursor.execute("select version()")
# fetch Only the first part of the data by using fetch one
data = cursor.fetcfone()
print(data)

# Create Table and Data base

# how to drop the data base just encase of needed its needed to drop
sql = '''drop database kgptalkie'''
cursor.execute(sql)

# create data base still need to be done by other teams
# example of creation of DB
sql = '''create database kgptalkie'''
cursor.execute(sql)

# connect in order to use data base
cursor.connection.commit()

sql = '''use kgptalkie'''
cursor.execute(sql)

# start cr5eating table person
sql = '''
create table person (
id int not null auto_increment,
fname text,
lname text,
primary key(id)
)
'''
cursor.execute(sql)

# insert data to the table
sql = '''
insert into person(fname, lname) values ('%s', '%s')''' % ('<fname FMI>', '<lname FMI>')
cursor.execute(sql)
db.commit()

# read what is on tables
sql = '''select * from person'''
cursor.execute(sql)
cursor.fetchall()

# in a case we want top describe the data base information we can use
sql = '''desc person'''
cursor.execute(sql)
cursor.fetchall()


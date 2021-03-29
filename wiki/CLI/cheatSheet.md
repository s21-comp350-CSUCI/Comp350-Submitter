# Quick reference 




## Return info for running ec2 instances
To return a table of ec2 instances including name, status, and ID of instance run  
* `aws ec2 describe-instances  --query "Reservations[*].Instances[*].{InstanceID:InstanceId,Name:Tags[?Key=='Name']|[0].Value,Status:State.Name}" --filters Name=instance-state-name,Values=running --output table`  

This will return the following
```
------------------------------------------------------
|                  DescribeInstances                 |
+----------------------+------------------+----------+
|      InstanceID      |      Name        | Status   |
+----------------------+------------------+----------+
|  i-09d9e102467dbd42c |  Bastion New     |  running |
|  i-0ea19faffe8a52a97 |  WebServerNew    |  running |
|  i-04a8a1679817aca4f |  3xNewAppServer  |  running |
+----------------------+------------------+----------+
```

## Start/stop-ing EC2 instances  
Run the following (assuming your own id values)  
* `aws ec2 start-instances --instance-ids  i-09d9e102467dbd42c, i-04a8a1679817aca4f --output table`  

For an output like this ( I added the table option after I had run the command once already, that's why previous state is same)  
```
---------------------------
|     StartInstances      |
+-------------------------+
||   StartingInstances   ||
|+-----------------------+|
||      InstanceId       ||
|+-----------------------+|
||  i-04a8a1679817aca4f  ||
|+-----------------------+|
|||    CurrentState     |||
||+--------+------------+||
|||  Code  |   Name     |||
||+--------+------------+||
|||  16    |  running   |||
||+--------+------------+||
|||    PreviousState    |||
||+--------+------------+||
|||  Code  |   Name     |||
||+--------+------------+||
|||  16    |  running   |||
||+--------+------------+||
||   StartingInstances   ||
|+-----------------------+|
||      InstanceId       ||
|+-----------------------+|
||  i-09d9e102467dbd42c  ||
|+-----------------------+|
|||    CurrentState     |||
||+--------+------------+||
|||  Code  |   Name     |||
||+--------+------------+||
|||  16    |  running   |||
||+--------+------------+||
|||    PreviousState    |||
||+--------+------------+||
|||  Code  |   Name     |||
||+--------+------------+||
|||  16    |  running   |||
||+--------+------------+||
```

To stop them   
`Run the following (assuming your own id values)  
* `aws ec2 start-instances --instance-ids  i-09d9e102467dbd42c, i-04a8a1679817aca4f --output table`  

## Return IP info for EC2 instances
We can run describe-instances using a query for public and private IP's
([reference](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-instances.html))  
* aws ec2 describe-instances  --query "Reservations[*].Instances[*].{PrivateIP:PrivateIpAddress,PublicIP:PublicIpAddress,Name:Tags[?Key=='Name']|[0].Value,Status:State.Name}" --filters Name=instance-state-name,Values=running --output table 

This returns something like  
```
---------------------------------------------------------------
|                      DescribeInstances                      |
+-----------------+-------------+------------------+----------+
|      Name       |  PrivateIP  |    PublicIP      | Status   |
+-----------------+-------------+------------------+----------+
|  Bastion New    |  10.0.1.97  |  54.160.194.0    |  running |
|  WebServerNew   |  10.0.1.9   |  174.129.12.196  |  running |
|  3xNewAppServer |  10.0.2.165 |  None            |  running |
+-----------------+-------------+------------------+----------+
```
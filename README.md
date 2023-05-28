# Get all the instance on your AWS cloud

### This script is use to fetch all the running instance  and give you an list of running instance with there details like instance ID, public IP, Private IP and instance type in the AWS account and also you can  delete the running instance by passing the name of the instance. 
------

### Please follow the below steps to run this script..

#### Step 1. You should have the Access key and Secret key of your AWS account or you can create this keys from the aws. Now you need to run the below command:


```
aws configure

````
Step 2. Now you need to install the boto3[ Python package] in your system and you can run the below command to have boto3 in your system.

```
pip3 install boto3

```

or you can install the requirements.txt file using the below command:
```
pip3 install requirements.txt
```
Step 3. Now you can run the python code using below command:

```
python3 fetch-instance.py
```
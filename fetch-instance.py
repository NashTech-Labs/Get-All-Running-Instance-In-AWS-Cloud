import boto3

# add your credential of AWS to interact with the AWS
aws_access_key_id = ''
aws_secret_access_key = ''
aws_region = ''

def list_running_EC2():
    # boto3 client
    ec2_client = boto3.client('ec2', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=aws_region)
    
    # to list the running instance in your aws account.
    response = ec2_client.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    

    # fetch all the details of the 
    Ec2 = response['Reservations']
    for reservation in Ec2:
        for instance in reservation['Instances']:
            Ec2_id = instance['InstanceId']
            Ec2_name = ''
            for tag in instance['Tags']:
                if tag['Key'] == 'Name':
                    Ec2_name = tag['Value']
                    break
            Ec2_type = instance['InstanceType']
            public_ip = instance.get('PublicIpAddress', 'N/A')
            private_ip = instance.get('PrivateIpAddress', 'N/A')
            print(f"Instance ID: {Ec2_id}, Instance Name: {Ec2_name}, Instance Type: {Ec2_type}, Public IP: {public_ip}, Private IP: {private_ip}")

def delete_instance_by_name(Ec2_name):
    # Create a Boto3 client for EC2
    ec2_client = boto3.client('ec2', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=aws_region)

    # Get the instance ID based on the instance name
    response = ec2_client.describe_instances(Filters=[{'Name': 'tag:Name', 'Values': [Ec2_name]}, {'Name': 'instance-state-name', 'Values': ['running']}])
    
    # Extract the instance ID
    if response['Reservations']:
        instance_id = response['Reservations'][0]['Instances'][0]['InstanceId']
        print(f"Instance found with name '{Ec2_name}', Instance ID: {instance_id}")

        # Ask for deletion confirmation
        delete = input(f"Delete instance '{Ec2_name}' with ID {instance_id}? (y/n): ")
        if delete.lower() == 'y':

            ec2_client.terminate_instances(InstanceIds=[instance_id])
            print(f"Instance {instance_id} terminated.")
        else:
            print(f"Instance {instance_id} not deleted.")
    else:
        print(f"No instance found with name '{Ec2_name}'.")

# calling the list_running_EC2 to get the list of the Ec2 instance in your AWS cloud
list_running_EC2()


# Calling the function to delete the EC2
Delete_EC2 = input("Please enter the name of your instance which you want to delete: ")
delete_instance_by_name(Delete_EC2)

# Dictionaries
# - Store and retrieve data using key-value pairs
# - Keys must be unique and immutable (e.g., strings, numbers, tuples)
# - Values can be of any data type
# - Useful for representing structured data like configurations, user profiles, etc.

# EC2 instance details
ec2_instance = {
    "InstanceId": "i-1234567890abcdef0",
    "InstanceType": "t2.micro",
    "State": "running",
    "PublicIpAddress": "203.0.111.2"
}

instance_id = ec2_instance["InstanceId"]
print(f"EC2 Instance ID: {instance_id}")

public_ip = ec2_instance.get("PublicIpAddress", "No Public IP")
print(f"Public IP Address: {public_ip}")

# Adding a new key-value pair
ec2_instance["AvailabilityZone"] = "eu-central-1a"
ec2_instance["State"] = "stopped"
print(f"Updated EC2 Instance Details: {ec2_instance}")

# Using pop to remove a key-value pair
removed_instance_type = ec2_instance.pop("InstanceType", "Not Found")
print(f"Removed Instance Type: {removed_instance_type}")
print(f"EC2 Instance Details after removal: {ec2_instance}")

# Using Delete to remove a key-value pair
del ec2_instance["AvailabilityZone"]
print(f"EC2 Instance Details after deleting Availability Zone: {ec2_instance}")